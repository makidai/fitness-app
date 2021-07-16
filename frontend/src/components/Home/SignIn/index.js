import React from "react";
import { useMutation } from "@apollo/client";
import gql from "graphql-tag";
import {
    Container,
    FormWrap,
    Icon,
    FormContent,
    Form,
    FormH1,
    FormLabel,
    FormInput,
    FormButton,
    Text,
} from "./SigninElements";

const SignIn = () => {
    const [tokenAuth] = useMutation(LOGIN_MUTATION, {
        onCompleted(data) {
            if (data?.tokenAuth?.token) {
                window.localStorage.setItem("token", data?.tokenAuth?.token);
                window.location.href = "/";
            } else {
                alert("メールアドレスもしくはパスワードに誤りがあります。");
            }
        },
    });

    return (
        <>
            <Container>
                <FormWrap>
                    <Icon to="/">Papurica</Icon>
                    <FormContent>
                        <Form action="#">
                            <FormH1>ログイン</FormH1>
                            <FormLabel htmlFor="for">メールアドレス</FormLabel>
                            <FormInput tyle="email" required />
                            <FormLabel htmlFor="for">パスワード</FormLabel>
                            <FormInput type="password" required />
                            <FormButton type="submit">ログイン</FormButton>
                            <Text>パスワードを忘れた場合</Text>
                        </Form>
                    </FormContent>
                </FormWrap>
            </Container>
        </>
    );
};

const LOGIN_MUTATION = gql`
    mutation LoginMutation($username: String!, $password: String!) {
        createUser(username: $username, password: $password) {
            user {
                id
                username
            }
        }
    }
`;

export default SignIn;
