package mutimod.effects;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.megacrit.cardcrawl.dungeons.AbstractDungeon;
import com.megacrit.cardcrawl.vfx.AbstractGameEffect;
import com.megacrit.cardcrawl.vfx.BorderFlashEffect;
import com.megacrit.cardcrawl.vfx.PetalEffect;
import com.megacrit.cardcrawl.vfx.SpotlightEffect;

public class MutiRageEffect extends AbstractGameEffect{
    private float timer = 0.1F;

    public MutiRageEffect() {
        this.duration = 2.0F;
    }

    public void update() {
        if (this.duration == 2.0F) {
            AbstractDungeon.effectsQueue.add(new SpotlightEffect());
            AbstractDungeon.effectsQueue.add(new BorderFlashEffect(Color.GOLD));
        }

        this.duration -= Gdx.graphics.getDeltaTime();
        this.timer -= Gdx.graphics.getDeltaTime();
        if (this.timer < 0.0F) {
            this.timer += 0.1F;
            AbstractDungeon.effectsQueue.add(new PetalEffect());
            AbstractDungeon.effectsQueue.add(new PetalEffect());
        }

        if (this.duration < 0.0F) {
            this.isDone = true;
        }
    }

    public void render(SpriteBatch spriteBatch) {

    }

    public void dispose() {

    }
}