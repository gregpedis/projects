package mutimod.cards;

import basemod.abstracts.CustomCard;
import basicmod.MutiMod;

import com.megacrit.cardcrawl.actions.animations.TalkAction;
import com.megacrit.cardcrawl.actions.common.GainBlockAction;
import com.megacrit.cardcrawl.cards.AbstractCard;
import com.megacrit.cardcrawl.characters.AbstractPlayer;
import com.megacrit.cardcrawl.core.CardCrawlGame;
import com.megacrit.cardcrawl.localization.CardStrings;
import com.megacrit.cardcrawl.monsters.AbstractMonster;

public class MutiSleep  extends CustomCard {
    public static final String ID = "MutiSleep";
    private static final CardStrings cardStrings;

    public MutiSleep() {
        super(ID, cardStrings.NAME, "basicmod/images/cards/skill/mutisleep.jpg", 0, cardStrings.DESCRIPTION, CardType.SKILL, CardColor.GREEN, CardRarity.RARE, CardTarget.SELF);
        MutiMod.logger.info("THIS IS MUTI SPEAKING");
        MutiMod.logger.info(cardStrings.DESCRIPTION);
        MutiMod.logger.info(cardStrings.UPGRADE_DESCRIPTION);
        this.baseBlock = 500;
        this.block = 500;
    }

    public void use(AbstractPlayer p, AbstractMonster m) {
        this.addToBot(new GainBlockAction(p,p, this.block));

        // this.addToBot(new SFXAction("VO_CULTIST_1A", -0.25f, true));
        this.addToBot(new TalkAction(true, "Can i turn off the lights?", 1.0F, 2.0F));
        // this.addToBot(new VFXAction(new MutiRageEffect(), 0.7F));
    }

    public void upgrade() {
        if (!this.upgraded) {
            this.upgradeName();
            this.upgradeBlock(499);
        }
    }

    public AbstractCard makeCopy() {
        return new MutiSleep();
    }

    static {
        cardStrings = new CardStrings();
        cardStrings.DESCRIPTION = "Gain !B! block.";
        cardStrings.NAME = "Muti Sleep";
    }
}
