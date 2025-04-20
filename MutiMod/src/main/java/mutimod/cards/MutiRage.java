package mutimod.cards;

import basemod.abstracts.CustomCard;
import mutimod.effects.MutiRageEffect;

import com.megacrit.cardcrawl.actions.AbstractGameAction;
import com.megacrit.cardcrawl.actions.animations.TalkAction;
import com.megacrit.cardcrawl.actions.animations.VFXAction;
import com.megacrit.cardcrawl.actions.common.DamageAction;
import com.megacrit.cardcrawl.actions.utility.SFXAction;
import com.megacrit.cardcrawl.cards.AbstractCard;
import com.megacrit.cardcrawl.cards.DamageInfo;
import com.megacrit.cardcrawl.characters.AbstractPlayer;
import com.megacrit.cardcrawl.core.CardCrawlGame;
import com.megacrit.cardcrawl.localization.CardStrings;
import com.megacrit.cardcrawl.monsters.AbstractMonster;

public class MutiRage  extends CustomCard {
    public static final String ID = "MutiRage";
    private static final CardStrings cardStrings;

    public MutiRage() {
        super(ID, "Muti Rage!", "basicmod/images/cards/attack/mutirage.jpg", 0, cardStrings.DESCRIPTION, CardType.ATTACK, CardColor.GREEN, CardRarity.RARE, CardTarget.ENEMY);
        this.baseDamage = 500;
    }

    public void use(AbstractPlayer p, AbstractMonster m) {
        this.addToBot(new DamageAction(m, new DamageInfo(p, this.damage, this.damageTypeForTurn), AbstractGameAction.AttackEffect.FIRE));

        this.addToBot(new SFXAction("VO_CULTIST_1A", -0.25f, true));
        this.addToBot(new TalkAction(true, "Greggy!!!", 1.0F, 2.0F));

        this.addToBot(new VFXAction(new MutiRageEffect(), 0.7F));
    }

    public void upgrade() {
        if (!this.upgraded) {
            this.upgradeName();
            this.upgradeDamage(499);
        }

    }

    public AbstractCard makeCopy() {
        return new MutiRage();
    }

    static {
        cardStrings = CardCrawlGame.languagePack.getCardStrings("Slice");
    }
}
