import React from "react";
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

export default SignIn;
