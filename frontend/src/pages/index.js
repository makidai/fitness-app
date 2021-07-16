import React, { useState } from "react";
import Navbar from "../components/Home/Navbar";
import Sidebar from "../components/Home/Sidebar";
import HeroSection from "../components/Home/HeroSection";
import InfoSection from "../components/Home/infoSection";
import Services from "../components/Home/Services";
import Footer from "../components/Home/Footer";
import { homeObjOne, homeObjTwo, homeObjThree } from "../components/Home/infoSection/Data";

const Home = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen);
    };

    return (
        <>
            <Sidebar isOpen={isOpen} toggle={toggle} />
            <Navbar toggle={toggle} />
            <HeroSection />
            <InfoSection {...homeObjOne} />
            <InfoSection {...homeObjTwo} />
            <Services />
            <InfoSection {...homeObjThree} />
            <Footer />
        </>
    );
};

export default Home;
