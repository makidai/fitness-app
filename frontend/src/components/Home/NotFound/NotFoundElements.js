import styled from "styled-components";
import { Link } from "react-router-dom";

export const NotFoundContainer = styled.div`
    background: #0c0c0c;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
    height: 800px;
`;

export const NotFoundText = styled.div`
    color: #fff;
    font-size: 24px;
`;

export const GoHomeLink = styled(Link)`
    color: #fff;
`;
