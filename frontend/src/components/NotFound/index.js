import React from "react";
import {
    NotFoundContainer,
    NotFoundText,
    GoHomeLink,
} from "./NotFoundElements";

const NotFound = () => {
    return (
        <NotFoundContainer>
            <NotFoundText>404 - Not Found！</NotFoundText>
            <GoHomeLink>
                <GoHomeLink to="/">➡︎ Go Home</GoHomeLink>
            </GoHomeLink>
        </NotFoundContainer>
    );
};

export default NotFound;
