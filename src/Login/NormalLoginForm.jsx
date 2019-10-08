/*eslint-disable */
import React from 'react';
import {
    Card,
    Form,
    Input,
    message,
    Button,
    Checkbox,
    Col,
    Icon,
    Modal
} from 'antd';
import './NormalLoginForm.css';
import { Switch, Route, NavLink, Redirect } from "react-router-dom"

const FormItem = Form.Item;

class NormalLoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: '',
            password: '',
        };
    }

    handleSubmit = (e) => {
        this.props.form.validateFields((err, values) => {
            let user = {
                username: this.props.form.getFieldValue('username'),
                password: this.props.form.getFieldValue('password')
            };
            if (user.password == '123456' && user.username == 'admin') { this.props.history.push('/home') }

        });

    };

    render() {
        const { getFieldDecorator } = this.props.form;
        return (
            <div>
                <div className="login-body">
                    <div className="login-mask">
                        <div>
                            <div className="logintest">
                                <Card
                                    title="登录"
                                    className="login-card"
                                    style={{
                                        MarginTop: '10px',
                                        MarginRight: '50px'
                                    }}>
                                    <Form style={{ width: 300 }}>
                                        <FormItem>
                                            {getFieldDecorator('username', {
                                                initialValue: '',
                                                rules: [
                                                    {
                                                        required: true,
                                                        message:
                                                            '用户名不能为空'
                                                    }
                                                ]
                                            })(
                                                <Input
                                                    prefix={
                                                        <Icon type="user" />
                                                    }
                                                    placeholder="请输入用户名:admin"
                                                />
                                            )}
                                        </FormItem>
                                        <FormItem>
                                            {getFieldDecorator('password', {
                                                initialValue: '',
                                                rules: [
                                                    {
                                                        required: true,
                                                        min: 6,
                                                        message:
                                                            '密码错误，不在长度范围内'
                                                    }
                                                ]
                                            })(
                                                <Input.Password
                                                    prefix={
                                                        <Icon type="lock" />
                                                    }
                                                    type="pass"
                                                    placeholder="请输入密码:123456"
                                                />
                                            )}
                                        </FormItem>
                                        <FormItem className="rememberpwd">
                                            <Button
                                                type="primary"
                                                onClick={(e) => this.handleSubmit(e)}
                                                style={{ float: 'right' }}>
                                                登录
                                                </Button>
                                        </FormItem>
                                    </Form>
                                </Card>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Form.create()(NormalLoginForm); // this.props.form才可以取到



