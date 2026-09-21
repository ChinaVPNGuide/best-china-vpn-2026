# 维护与核验

## 内容依据

最近资料核对：2026-09-21。维护者为 ZibVPN 团队，不将自家介绍称为独立评测。

- 套餐、总价、设备数、每日流量：[官方套餐页](https://zibvpn.com/zh/pricing)。
- 1 GB 注册试用：[注册页](https://zibvpn.com/zh/register)。期限及账户权益需另核对。
- 退款、续费、账户共享：[用户协议](https://zibvpn.com/zh/terms)第 3、4 节。
- 客户端版本：[下载页](https://zibvpn.com/zh/download)；Linux beta、架构、依赖及桌面限制：[Linux 页](https://zibvpn.com/zh/download/linux)。
- ChatGPT 支持范围与故障：[支持列表](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)、[排错说明](https://help.openai.com/en/articles/7996703-troubleshooting-chatgpt-error-messages)。
- YouTube：[播放故障](https://support.google.com/youtube/answer/3037019?hl=zh-Hans)、[调试信息](https://support.google.com/youtube/answer/7519898?hl=zh-Hans)。
- 协议：[XTLS/REALITY](https://github.com/XTLS/REALITY)。

更新日期仅在实质修改和重新核对资料时调整。无可复核日志，不写新的“实测日期”、可用率、跨运营商或竞品性能名次。真实测试需记录日期、设备、版本、网络、任务与失败样本，并移除连接凭据及个人信息。

## 官网到站归因

- README：`utm_source=github`。
- Pages：`utm_source=github_pages`。
- 两者：`utm_medium=referral`，本次 `utm_campaign=20260921_repo_refresh`。
- `utm_content` 为文档与链接位置，例如 `index_top`、`linux-vpn_top`。
- 本次按文件类型区分；读者在 GitHub 直接阅读某篇 Pages 源码并点击链接时，仍会带 github_pages。需要与 referrer 交叉解读，不能当作精确浏览界面识别。
- 不在本仓库新增跟踪脚本。用既有官网统计查看来源、UTM、落地页及后续事件；各维度不可相加当去重访客。
- 核验官网页面时使用无 UTM 地址；自检、机器人、已有客户与真实新增访问需尽量区分，无法区分就记录限制。

## 发布检查

1. 确认远端新提交与本地更改，没有覆盖其他维护者的工作。
2. 保留已有 permalink 和站点 baseurl，检查首页与全部专题互链。不要把 `./topic` 写入有尾斜杠的子页面，它会解析到该子目录。
3. 构建 Jekyll，运行 `python3 scripts/check_site.py /path/to/generated/site`，检查 sitemap、canonical、文档链接与追踪参数。
4. 桌面和手机宽度查看表格、标题及主要官网入口；模板改动另外复核。
5. 公开内容按项目授权流程确认后发布，检查 Pages 部署结果及实际页面。原提交保留以便回退。

`robots.txt` 置于项目子路径，不控制整个 github.io 域名的抓取策略。不得将它当作域名根目录 robots 配置或已被搜索引擎收录的证明。

发布后在下一次获授权复盘中比较完整 7 天窗口的官网到站、来源和 UTM，再看注册/付款质量。GitHub Traffic 是仓库浏览，不包含 Pages 的完整访问统计；不得用它直接计算官网转化率。没有默认定时运行或自动发布任务。
