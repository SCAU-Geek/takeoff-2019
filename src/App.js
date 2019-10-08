import React from 'react';
import ReactDOM from 'react-dom';
import { ConfigProvider, DatePicker, message, Timeline } from 'antd';
// 由于 antd 组件的默认文案是英文，所以需要修改为中文
import zhCN from 'antd/es/locale/zh_CN';
import moment from 'moment';
import 'moment/locale/zh-cn';
import 'antd/dist/antd.css';
import './index.css';
import { HashRouter, Route, Switch, Redirect } from "react-router-dom";
import Login from './Login/NormalLoginForm.jsx';
import Home from './Home.js';
moment.locale('zh-cn');

export default class App extends React.Component {
  render() {
    return (
        <HashRouter>
            <Switch>
                <Redirect exact from="/" to="/login"></Redirect>
                <Route path="/login" component={Login}></Route>
                <Route path="/home" component={Home}></Route>
            </Switch>
        </HashRouter>
    )
}


}