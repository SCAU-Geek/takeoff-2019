import React from 'react';
import { Menu, Icon, Layout } from 'antd';
import { ConfigProvider, DatePicker, message, Timeline } from 'antd';
import './Home.css'
import zhCN from 'antd/es/locale/zh_CN';
import 'moment/locale/zh-cn';
import 'antd/dist/antd.css';
import moment from 'moment';
import { PageHeader, Dropdown, Button, Tag, Typography, Row } from 'antd';
moment.locale('zh-cn');

const { Content, Sider, Header } = Layout;

const { Paragraph } = Typography;

const menu = (
    <Menu>
        <Menu.Item>
            <a target="_blank" rel="noopener noreferrer" href="http://www.alipay.com/">
                1st menu item
      </a>
        </Menu.Item>
        <Menu.Item>
            <a target="_blank" rel="noopener noreferrer" href="http://www.taobao.com/">
                2nd menu item
      </a>
        </Menu.Item>
        <Menu.Item>
            <a target="_blank" rel="noopener noreferrer" href="http://www.tmall.com/">
                3rd menu item
      </a>
        </Menu.Item>
    </Menu>
);

const DropdownMenu = () => {
    return (
        <Dropdown key="more" overlay={menu}>
            <Button
                style={{
                    border: 'none',
                    padding: 0,
                }}
            >
                <Icon
                    type="ellipsis"
                    style={{
                        fontSize: 20,
                        verticalAlign: 'top',
                    }}
                />
            </Button>
        </Dropdown>
    );
};

const routes = [
    {
        path: 'index',
        breadcrumbName: 'First-level Menu',
    },
    {
        path: 'first',
        breadcrumbName: 'Second-level Menu',
    },
    {
        path: 'second',
        breadcrumbName: 'Third-level Menu',
    },
];

const IconLink = ({ src, text }) => (
    <a
        style={{
            marginRight: 16,
            display: 'flex',
            alignItems: 'center',
        }}
    >
        <img
            style={{
                marginRight: 8,
            }}
            src={src}
            alt="start"
        />
        {text}
    </a>
);

const content = (
    <div className="content">
        <Paragraph>
            本项目为使用react框架搭建的静态页面，使用的组件库为ant design，可实现查看hhj某一天的课程功能。
    </Paragraph>
        <Paragraph>
            由于hhj太过弱鸡的原因，没有学过python爬虫爬数据，主要学习的内容为前端的内容，所以本次的网页为静态页面，
            周三满课可能没时间进一步完善网站，但还是希望可以加入到工作室当中去，接受大佬们的教导,多学习一点前后端技术。
            以下点击选择日期即可展示出当天的课程表。
    </Paragraph>
        <Row className="contentLink" type="flex">
            <IconLink
                src="https://gw.alipayobjects.com/zos/rmsportal/MjEImQtenlyueSmVEfUD.svg"
                text=""
            />
            <IconLink
                src="https://gw.alipayobjects.com/zos/rmsportal/NbuDUAuBlIApFuDvWiND.svg"
                text=" "
            />
            <IconLink
                src="https://gw.alipayobjects.com/zos/rmsportal/ohOEPSYdDTNnyMbGuyLb.svg"
                text=""
            />
        </Row>
    </div>
);

const CContent = ({ children, extraContent }) => {
    return (
        <Row className="content" type="flex">
            <div className="main" style={{ flex: 1 }}>
                {children}
            </div>
            <div
                className="extra"
                style={{
                    marginLeft: 80,
                }}
            >
                {extraContent}
            </div>
        </Row>
    );
};


export default class Home extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            date: moment('2009-10-6', 'YYYY-MM-DD'),
            date_string: 0,//时间戳
            lesson_sum: 0,
            select_week: 1,
            select_day: 1,
            _display1: 'block',
            start_time_string: [0, 1567353600000, 1567958400000, 1568563200000, 1569168000000, 1569772800000, 1570377600000,
                1570982400000, 1571587200000, 1572192000000, 1572796800000, 1573401600000, 1574006400000,
                1574611200000, 1575216000000, 1575820800000, 1576425600000],
            end_time_string: [0, 1567958399000, 1568563199000, 1569167999000, 1569772799000, 1570377599000, 1570982399000,
                1571587199000, 1572191999000, 1572796799000, 1573401599000, 1574006399000, 1574611199000,
                1575215999000, 1575820799000, 1576425599000, 1577030399000],
            list: []
        }
    }

    componentWillMount = () => {
        var today_date = new Date();
        let a = today_date.valueOf();
        this.main_function(today_date.valueOf());
        this.setState({
            date: moment(today_date, 'YYYY-MM-DD'),
            date_string: today_date.valueOf()
        })
    }

    handleChange = date => {
        message.info(`您选择的日期是: ${date ? date.format('YYYY-MM-DD') : '未选择'}`);
        this.setState({ date });
        this.setState({ date_string: date.valueOf() });
        this.main_function(date.valueOf());

    };

    main_function = (a) => {
        var one_day = 86400000;//一天的毫秒数
        var flag = 1;
        //非教学周
        if (a < this.state.start_time_string[1] || a > this.state.end_time_string[16]) {
            this.setState({ lesson_sum: 0, _display1: 'none' })
            message.error('非常舒服，当天没有课程')
            flag = 0;
        }
        //周末
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a <= this.state.end_time_string[i] && a >= this.state.end_time_string[i] - 172799000) {
                    this.setState({ lesson_sum: 0, _display1: 'none' });
                    message.error('非常舒服，当天没有课程');
                    flag = 0;
                    break;

                }
            }
        }

        //周一
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a >= this.state.start_time_string[i] && a < this.state.start_time_string[i] + one_day) {
                    this.setState({
                        lesson_sum: 0, _display1: 'block',
                        list: ['第3-4节 10:05-11:40 体育跃进南蓝球场1', '第7-8节 14:30-16:05 离散结构4303'],
                        lesson_sum: 2,
                        select_week: i,
                        select_day: 1,
                    });
                    flag = 0;
                    break;
                }
            }
        }

        //周二
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a >= this.state.start_time_string[i] + one_day && a < this.state.start_time_string[i] + one_day * 2) {
                    if (i <= 8) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第1-2节 8:00-9:35 概率论4208', '第3-4节 10:05-11:40 毛概4407', '第9-10节 16:35-18:10 数电4407'],
                            lesson_sum: 3,
                            select_week: i,
                            select_day: 2,
                        });
                        flag = 0;
                        break;
                    }
                    else if (i <= 14) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第3-4节 10:05-11:40 毛概4407', '第9-10节 16:35-18:10 数电4407'],
                            lesson_sum: 2,
                            select_week: i,
                            select_day: 2,
                        });
                        flag = 0;
                        break;
                    }
                    else if (i <= 16) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第3-4节 10:05-11:40 毛概4407'],
                            lesson_sum: 1,
                            select_week: i,
                            select_day: 2,
                        });
                        flag = 0;
                        break;
                    }
                }
            }
        }

        //周三
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a >= this.state.start_time_string[i] + one_day * 2 && a < this.state.start_time_string[i] + one_day * 3) {
                    if (i <= 5) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第7-8节 14:30-16:05 离散结构4105', '第9-10节 16:35-18:10 大学生创新创业基础4511', '第11-12节 19:30-21:05 毛概4208'],
                            lesson_sum: 3,
                            select_week: i,
                            select_day: 3,
                        });
                        flag = 0
                        break;
                    }
                    else {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第1-2节 8:00-9:35 面对对象程序设计', '第5-6节 12:30-14:05 面对对象程序设计', '第7-8节 14:30-16:05 离散结构4105', '第9-10节 16:35-18:10 大学生创新创业基础4511', '第11-12节 19:30-21:05 毛概4208'],
                            lesson_sum: 5,
                            select_week: i,
                            select_day: 3,
                        });
                        flag = 0
                        break;
                    }
                }
            }
        }
        //周四
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a >= this.state.start_time_string[i] + one_day * 3 && a < this.state.start_time_string[i] + one_day * 4) {
                    this.setState({
                        lesson_sum: 0, _display1: 'block',
                        list: ['第3-4节 10:05-11:40 大学英语4603', '第7-8节 14:30-16:05 英语阅读技能讲与练4612'],
                        lesson_sum: 2,
                        select_week: i,
                        select_day: 4,
                    });
                    flag = 0
                    break;
                }
            }
        }
        //周五
        if (flag) {
            for (let i = 1; i <= 16; i++) {
                if (a >= this.state.start_time_string[i] + one_day * 4 && a < this.state.start_time_string[i] + one_day * 5) {
                    if (i <= 6) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第1-2节 8:00-9:35 概率论4305', '第3-4节 10:05-11:40 数电4107', '第5-6节 12:30-14:05 面对对象程序设计'],
                            lesson_sum: 3,
                            select_week: i,
                            select_day: 5,
                        });
                        flag = 0
                        break;
                    }
                    else if (i <= 8) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第1-2节 8:00-9:35 概率论4305', '第3-4节 10:05-11:40 数电4107', '第5-6节 12:30-14:05 面对对象程序设计', '第9-10节 16:35-18:10 数电'],
                            lesson_sum: 4,
                            select_week: i,
                            select_day: 5,
                        });
                        flag = 0
                        break;
                    }
                    else if (i <= 14) {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第3-4节 10:05-11:40 数电4107', '第5-6节 12:30-14:05 面对对象程序设计', '第9-10节 16:35-18:10 数电'],
                            lesson_sum: 3,
                            select_week: i,
                            select_day: 5,
                        });
                        flag = 0
                        break;
                    }
                    else {
                        this.setState({
                            lesson_sum: 0, _display1: 'block',
                            list: ['第5-6节 12:30-14:05 面对对象程序设计'],
                            lesson_sum: 1,
                            select_week: i,
                            select_day: 5,
                        });
                        flag = 0
                        break;
                    }
                }
            }
        }
    }

    componentWillUpdate = () => {
        // console.log(this.state.date.valueOf());
        // console.log(this.state.date_string);
    }

    render() {
        const { date } = this.state;
        var count = 1;
        return (
            <div>
                <div className="toptop">
                    <PageHeader
                        title="hhj"
                        subTitle="实现查看课程表功能"
                        tags={<Tag color="blue">Running</Tag>}
                        extra={[

                            <Button key="2">Operation</Button>,
                            <Button key="1" type="primary">Primary</Button>,
                            <DropdownMenu key="more" />,
                        ]}
                        avatar={{ src: 'https://avatars1.githubusercontent.com/u/8186664?s=460&v=4' }}
                    >
                        <CContent
                            extraContent={
                                <img
                                    src="https://gw.alipayobjects.com/mdn/mpaas_user/afts/img/A*KsfVQbuLRlYAAAAAAAAAAABjAQAAAQ/original"
                                    alt="content"
                                />
                            }
                        >
                            {content}
                        </CContent>
                    </PageHeader>
                </div>
                <ConfigProvider locale={zhCN}>
                    <div style={{ width:'50%', margin: '10px auto' }}>
                        <DatePicker onChange={this.handleChange} defaultValue={this.state.date} size="large"/>
                        <div style={{ marginTop: 20, marginBottom: 20 }} className="Timeline_head">
                            当前课表为第{this.state.select_week}周星期{this.state.select_day} 日期为:{date ? date.format('YYYY-MM-DD') : '未选择'}的课程,总共有{this.state.lesson_sum}节课
              </div>
                        <Timeline style={{ display: this.state._display1 }} className="Timeline">
                            {(this.state.list || []).map((item, index) => (
                                <Timeline.Item key={Math.random()} className="Timeline_child">
                                    {this.state.list[index]}
                                </Timeline.Item>
                            ))}
                        </Timeline>
                    </div>

                </ConfigProvider>

            </div>)
    }
}
