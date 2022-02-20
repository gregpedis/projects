import os
from bs4 import Tag
from bs4.element import ResultSet
from bs4 import BeautifulSoup as Soupa

html: str = "items.txt"
output_directory: str = "items"


class Item:
    def __init__(self, id: int, name: str, recipes: list = None):
        self.id = id
        self.name = name.strip()
        self.recipes = recipes if recipes is not None else []

    def __repr__(self) -> str:
        return self._stringify()

    def __str__(self) -> str:
        return self._stringify()

    def _stringify(self):
        pretty = f"<Item {str(vars(self))}>"


def soupify(html_file: str) -> Soupa:
    with open(html_file) as fd:
        html = fd.read()
        soup = Soupa(html, "html.parser")
        return soup


def get_item_rows(soup: Soupa) -> ResultSet:
    target_classes = {"class": ["sortable", ]}
    table: Tag = soup.find("table", attrs=target_classes)
    body: Tag = table.find("tbody")
    rows = body.find_all("tr", recursive=False)
    return rows


def generate_items(item_rows: ResultSet) -> list:
    items = [generate_item(ir) for ir in item_rows[1:]]
    return items


def generate_item(item_row: Tag) -> Item:
    tds = item_row.find_all("td", recursive=False)
    item_name = tds[0].span.text
    item_id = tds[1].text
    recipes = generate_recipes(tds[2:])
    item = Item(int(item_id), item_name, recipes)
    return item


def generate_recipes(recipes_data: list) -> list:
    recipe_rows = [rd.table.tbody.find_all("tr") for rd in recipes_data]
    recipes = [generate_recipe(rr) for rr in recipe_rows]
    return recipes


def generate_recipe(recipe_rows: ResultSet) -> list:
    components = [td.a["title"] for tr in recipe_rows
                  for td in tr.find_all("td", Recursive=False)]
    components = [c[:c.find("(")].strip() for c in components]
    return components


def persist_items(items: list, target_directory: str) -> None:
    for item in items:
        filename = generate_valid_filename(item.name)
        path = os.path.join(target_directory, filename)
        prefix_lines = [f"[ID]: {item.id}\n",
                        f"[NAME]: {item.name}\n",
                        "\n",
                        "[RECIPES]\n"]
        recipe_lines = [" ; ".join(components) +
                        "\n" for components in item.recipes]
        with open(path, "wt") as fd:
            fd.writelines(prefix_lines)
            fd.writelines(recipe_lines)


def generate_valid_filename(item_name: str) -> str:
    item_name = item_name.strip()
    invalids = [" ", "'", "/", "\\", ":", "*", "?", '"', "<", ">"]
    for invalid in invalids:
        item_name = item_name.replace(invalid, "_")
    return item_name + ".txt"


def main():
    assert os.path.exists(html), "Please specify a valid html file."
    assert os.path.exists(
        output_directory), "Please specify a valid output directory."
    soup = soupify(html)
    item_rows = get_item_rows(soup)
    items = generate_items(item_rows)
    persist_items(items, output_directory)


if __name__ == "__main__":
    main()
