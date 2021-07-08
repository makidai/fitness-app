import React from "react";
import Icon1 from '../../images/svg-1.svg'
import Icon2 from '../../images/svg-2.svg'
import Icon5 from '../../images/svg-5.svg'
import {
    ServicesContainer,
    ServicesH1,
    ServicesH2,
    ServicesWrapper,
    ServicesCard,
    ServicesIcon,
	ServicesP
} from "./ServicesElements";

const Services = () => {
    return (
        <ServicesContainer id="services">
            <ServicesH1>Our Services</ServicesH1>
            <ServicesWrapper>
                <ServicesCard>
                    <ServicesIcon src={Icon1} />
                    <ServicesH2>栄養管理</ServicesH2>
                    <ServicesP>身体づくりに必要な栄養管理をサポート</ServicesP>
                </ServicesCard>
                <ServicesCard>
                    <ServicesIcon src={Icon2} />
                    <ServicesH2>筋トレ</ServicesH2>
                    <ServicesP>効果的な筋トレとモチベーション維持をサポート</ServicesP>
                </ServicesCard>
                <ServicesCard>
                    <ServicesIcon src={Icon5} />
                    <ServicesH2>ライフスタイル</ServicesH2>
                    <ServicesP>美容やファッションなどライフスタイルをサポート</ServicesP>
                </ServicesCard>
            </ServicesWrapper>
        </ServicesContainer>
    );
};

export default Services;
