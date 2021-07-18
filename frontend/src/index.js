import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import {
    ApolloClient,
    ApolloProvider,
    createBatchingNetworkInterface,
} from "react-apollo";

const networkInterface = createBatchingNetworkInterface({
    uri: "http://localhost:8000/gql",
    batchInterval: 10,
    opts: {
        credentials: "same-origin",
    },
});

const client = new ApolloClient({
    networkInterface: networkInterface,
});

ReactDOM.render(
    <ApolloProvider client={client}>
        <App />
    </ApolloProvider>,
    document.getElementById("root")
);
