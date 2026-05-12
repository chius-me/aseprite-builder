<p align="right">
  English | <a href="./README.zh.md">简体中文</a>
</p>

<h1 align="center">Aseprite Builder</h1>

<p align="center">
  A GitHub Actions workflow for building Aseprite on Windows x64 for personal use.
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-Workflow-2088FF.svg">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-x64-0078D4.svg">
  <img alt="Aseprite" src="https://img.shields.io/badge/Aseprite-Builder-7D929E.svg">
</p>

## Overview

This repository contains a manually triggered GitHub Actions workflow for building [Aseprite](https://github.com/aseprite/aseprite) on Windows x64.

It contains only the build workflow, tests, and documentation. It does not contain Aseprite source code, Aseprite assets, Skia binaries, build outputs, or release binaries.

## Why This Exists

Aseprite can be compiled from source, but the Windows build needs a matching Skia package and a correctly configured MSVC/Ninja environment. This repository keeps that setup in one reusable workflow.

## Important License Notice

Aseprite is not licensed by this repository. Aseprite source code and official binaries are governed by the official [Aseprite EULA](https://github.com/aseprite/aseprite/blob/main/EULA.txt).

The MIT License in this repository applies only to this builder workflow, tests, and documentation.

Before using this workflow, read and follow the Aseprite EULA. In particular, do not publicly distribute binaries produced by this workflow unless you have the rights to do so.

## Disclaimer

This project is an independent community-maintained builder script and is not affiliated with, endorsed by, or sponsored by Igara Studio or the Aseprite project.

If this repository infringes any rights of Aseprite or its maintainers, please contact contact@chius.cc and I will address it promptly.

## Usage

1. Fork this repository or copy the workflow into your own private repository.
2. Open the repository on GitHub.
3. Go to **Actions**.
4. Select **Build Aseprite Windows**.
5. Click **Run workflow**.
6. Set `aseprite_ref` to the Aseprite branch, tag, or commit you want to build.
7. Download the `Aseprite-Windows-x64` artifact from the completed workflow run for your personal use.

The default `aseprite_ref` is `main`, which tracks upstream Aseprite development. For repeatable builds, use a specific Aseprite tag or commit SHA.

## Workflow

The workflow:

- Checks out `aseprite/aseprite` with recursive submodules.
- Installs Ninja using `aseprite/get-ninja`.
- Sets up the Visual Studio x64 developer environment.
- Resolves the matching Windows x64 Skia package using Aseprite's `laf/misc/skia-url.sh` helper.
- Configures Aseprite with CMake and the Skia backend.
- Disables updater/news/OpenSSL options that can introduce unwanted runtime dependencies.
- Builds the `aseprite` target.
- Verifies `aseprite.exe` exists.
- Audits for Git/OpenSSL runtime DLL dependencies.
- Uploads the build directory as a workflow artifact.

## Repository Contents

```text
.github/workflows/build.yml  Windows x64 build workflow
tests/test_workflow.py       Workflow safety checks
README.md                    English documentation
README.zh.md                 Simplified Chinese documentation
LICENSE                      License for this builder repository
```

## Troubleshooting

### Skia Download Fails

Use an Aseprite ref that includes the expected `laf/misc/skia-url.sh` helper and matching submodule metadata. Tags or commits from upstream Aseprite are usually safer than arbitrary branches from forks.

### CMake Cannot Find Skia

Check the `Download matching Skia` step logs. The workflow expects `skia/out/Release-x64/skia.lib` after extraction.

### Build Exceeds The Timeout

Re-run the workflow. GitHub-hosted Windows runners can vary in performance. If this happens often, raise `timeout-minutes` in `.github/workflows/build.yml`.

### OpenSSL Runtime Dependency Audit Fails

The workflow intentionally fails if `aseprite.exe` depends on Git-provided OpenSSL DLLs. Keep `-DENABLE_NEWS=OFF`, `-DENABLE_UPDATER=OFF`, and `-DENABLE_OPENSSL=OFF` unless you understand the runtime packaging implications.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE).

This license does not apply to Aseprite itself. See the official [Aseprite EULA](https://github.com/aseprite/aseprite/blob/main/EULA.txt).
