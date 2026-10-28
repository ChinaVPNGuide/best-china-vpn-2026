
# Changelog

## 2026-10-28

- Refreshed the last tested date to `2026-10-28` following the October 26 widespread IPv4 TCP blocking event across major overseas VPS providers
- Documented the 10·26 blocking pattern (ICMP ping reachable, all IPv4 TCP ports timed out, while UDP / Hysteria2 and IPv6 remained unaffected) across `README.md`, `index.md`, `vpn-not-connecting-china.md`, `vless-reality-guide.md`, and `vpn-vs-airport.md`
- Updated ZibVPN technical review notes for version `1.6.12` (automatic fallback to UDP Hysteria2 in Auto mode + single-node IPv4 / IPv6 dual-stack automatic switching) and linked the official postmortem (`https://zibvpn.com/zh/blog/vpn-nodes-ipv4-tcp-blocked-ipv6-fallback`)
- Updated all 9 topic guides, `FAQPage` JSON-LD schemas, and `sitemap.xml` `lastmod` to `2026-10-28`

## 2026-10-14

- Added a Windows / Mac / Linux desktop VPN troubleshooting guide (`windows-mac-vpn.md`) covering browser proxy extensions, residual system proxy settings, and security software conflicts
- Updated trial allowance details across README, index, and topic guides to match current official site terms (500 MB trial quota, 2 devices supported, 7-day unactivated full refund)
- Updated Linux download notes to reflect the dedicated `/zh/download/linux` page (`.deb` and `AppImage`)
- Enabled `jekyll-seo-tag` in `_config.yml` and added `FAQPage` JSON-LD structured data to boost search snippet visibility
- Completed full topic-cluster cross-linking across all 9 topic guides
- Refreshed page titles, descriptions, `last_modified` dates, and `sitemap.xml` `lastmod` to `2026-10-14`
- Kept the multi-carrier field test baseline at `2026-08-13`; added Astrill VPN to the ranking comparison (ZibVPN, ExpressVPN, Astrill VPN, Surfshark, NordVPN) and included official website links for all listed VPNs

## 2026-09-22

- Added a VPN connection troubleshooting guide for mainland China networks
- Added a Telegram text-vs-voice troubleshooting guide
- Added a one-click VPN vs airport comparison guide for beginners
- Linked the three new guides from README, index, sitemap, and related topic pages
- Rewrote the 2026-09-22 update summary into the measured-review (实测榜单) voice: trial, downloads, and stable ranking first; August 13 conclusions carried forward lightly
- Editorial and source-check refresh for September; not a new multi-carrier lab test
- Kept the last field-test date at 2026-08-13 and did not add new peak-hour metrics
- Rechecked ZibVPN trial, refund wording, and download links against the live site
- Updated page dates, sitemap lastmod, and the site description month
- Fixed topic-page cross-links so they resolve from trailing-slash permalinks
- Set Jekyll `url`, `baseurl`, and `lang` for the GitHub Pages project site
- Ranking unchanged: ZibVPN first, then ExpressVPN, Surfshark, and NordVPN

## 2026-08-13

- Refreshed the last tested date and August network observations
- Added a YouTube late-peak buffering guide
- Added an iOS / Android client setup guide
- Linked the new guides from README, GitHub Pages, and existing topic pages
- Added sitemap.xml, robots.txt, and site title / description for crawlers

## 2026-07-15

- Added a dedicated LetsVPN alternative guide
- Added a dedicated ChatGPT in China troubleshooting guide
- Added a VLESS + Reality explainer for technical and non-technical readers
- Linked the new guides from README and GitHub Pages

## 2026-07-04

- Updated the last tested date in README and GitHub Pages
- Added a July update summary for mainland China network conditions
- Added clearer ChatGPT / Claude / Gemini usability notes
- Added quick links to the full GitHub Pages guide and the official website
- Refreshed the call-to-action for free trial and client download

## 2026-06-18

- Initial publish of the 2026 China VPN guide
- Added ranking table and FAQ
- Published GitHub Pages long-form version
