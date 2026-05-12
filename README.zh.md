<p align="right">
  <a href="./README.md">English</a> | 简体中文
</p>

<h1 align="center">Aseprite Builder</h1>

<p align="center">
  用于在 Windows x64 上通过 GitHub Actions 编译 Aseprite 的个人自建工作流。
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-Workflow-2088FF.svg">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-x64-0078D4.svg">
  <img alt="Aseprite" src="https://img.shields.io/badge/Aseprite-Builder-7D929E.svg">
</p>

## 项目简介

这个仓库提供一个手动触发的 GitHub Actions 工作流，用于在 Windows x64 上编译 [Aseprite](https://github.com/aseprite/aseprite)。

本仓库只包含构建工作流、测试和文档，不包含 Aseprite 源码、Aseprite 资源、Skia 二进制包、构建产物或发布二进制文件。

## 为什么需要这个仓库

Aseprite 可以从源码编译，但 Windows 构建需要匹配的 Skia 包，以及正确配置的 MSVC/Ninja 环境。这个仓库把这些步骤整理成一个可复用的工作流。

## 重要协议说明

Aseprite 不由本仓库授权。Aseprite 源码和官方二进制文件遵循官方 [Aseprite EULA](https://github.com/aseprite/aseprite/blob/main/EULA.txt)。

本仓库的 MIT License 只适用于这个 builder 工作流、测试和文档。

使用这个工作流前，请阅读并遵守 Aseprite EULA。尤其是，除非你拥有相应权利，否则不要公开分发由该工作流生成的二进制文件。

## 免责声明

本项目是独立维护的社区构建脚本，与 Igara Studio 或 Aseprite 项目不存在从属、认可或赞助关系。

如果本仓库侵犯了 Aseprite 或其维护者的任何权益，请联系 contact@chius.cc，我会及时处理。

## 使用方法

1. Fork 本仓库，或把工作流复制到你自己的私有仓库。
2. 在 GitHub 打开该仓库。
3. 进入 **Actions**。
4. 选择 **Build Aseprite Windows**。
5. 点击 **Run workflow**。
6. 将 `aseprite_ref` 设置为你要编译的 Aseprite 分支、标签或 commit。
7. 工作流完成后，下载 `Aseprite-Windows-x64` artifact 供个人使用。

默认的 `aseprite_ref` 是 `main`，会跟随上游 Aseprite 开发分支。为了获得可复现构建，建议使用指定的 Aseprite tag 或 commit SHA。

## 工作流内容

该工作流会：

- 使用 recursive submodules 检出 `aseprite/aseprite`。
- 使用 `aseprite/get-ninja` 安装 Ninja。
- 配置 Visual Studio x64 开发环境。
- 使用 Aseprite 自带的 `laf/misc/skia-url.sh` 解析匹配的 Windows x64 Skia 包。
- 使用 CMake 和 Skia 后端配置 Aseprite。
- 关闭 updater/news/OpenSSL 选项，避免引入不必要的运行时依赖。
- 构建 `aseprite` 目标。
- 检查 `aseprite.exe` 是否存在。
- 审计 Git/OpenSSL 运行时 DLL 依赖。
- 将构建目录上传为 workflow artifact。

## 仓库内容

```text
.github/workflows/build.yml  Windows x64 构建工作流
tests/test_workflow.py       工作流安全检查
README.md                    英文文档
README.zh.md                 简体中文文档
LICENSE                      本 builder 仓库的授权协议
```

## 故障排查

### Skia 下载失败

请使用包含 `laf/misc/skia-url.sh` 辅助脚本和匹配 submodule 元数据的 Aseprite ref。通常上游 Aseprite 的 tag 或 commit 会比 fork 中的任意分支更可靠。

### CMake 找不到 Skia

检查 `Download matching Skia` 步骤日志。工作流解压后预期存在 `skia/out/Release-x64/skia.lib`。

### 构建超时

重新运行工作流。GitHub 托管的 Windows runner 性能可能波动。如果经常发生，可以提高 `.github/workflows/build.yml` 中的 `timeout-minutes`。

### OpenSSL 运行时依赖审计失败

如果 `aseprite.exe` 依赖 Git 提供的 OpenSSL DLL，工作流会主动失败。除非你理解运行时打包影响，否则请保留 `-DENABLE_NEWS=OFF`、`-DENABLE_UPDATER=OFF` 和 `-DENABLE_OPENSSL=OFF`。

## License

本仓库使用 MIT License。详见 [LICENSE](LICENSE)。

该协议不适用于 Aseprite 本身。请查看官方 [Aseprite EULA](https://github.com/aseprite/aseprite/blob/main/EULA.txt)。
