import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import {
    ApolloClient,
    InMemoryCache,
    ApolloProvider,
    createHttpLink,
} from "@apollo/client";
import { setContext } from "@apollo/client/link/context";

const httpLink = createHttpLink({
    uri: "http://127.0.0.1:8000/graphql/",
});

const authLink = setContext((_, { headers }) => {
    const token = window.localStorage.getItem("token");
    return {
        headers: {
            ...headers,
            authorization: token ? `JWT ${token}` : "",
        },
    };
});

const client = new ApolloClient({
    uri: authLink.concat(httpLink),
    cache: new InMemoryCache(),
});

ReactDOM.render(
    <ApolloProvider client={client}>
        <App />
    </ApolloProvider>,
    document.getElementById("root")
);
