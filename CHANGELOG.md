# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## v3.0.0b2 (2020-02-12)

### Added

- Support for establishing TLS connections by checking the first byte of the
  request for a TLS handshake. This allows for both plaintext and encrypted
  communication to be made over the same port. A TLS section has been added to
  the default pygopherd configuration file.
- Several protocols which take advantage of the new TLS connections.
    - rfc1436.SecureGopherProtocol (gopher + TLS).
    - gopherp.SecureGopherPlusProtocol (gopher plus + TLS).
    - http.HTTPSProtocol (http + TLS).
    - gemini.GeminiProtocol (https://gemini.circumlunar.space/).
- Display server version with ``pygopherd --version``.

### Changed

- Gracefully handle OS errors when calling ``setpgrp()``.
- Refactored the socket server classes and added additional test cases.

## v3.0.0b1 (2020-01-18)

### Added

- Support for python 3.7+.
- Additional test coverage and type hints.
- Published package to PyPI (https://pypi.org/project/pygopherd/).

### Changed

- Significant sprucing up of the codebase.
- Numerous minor bugs were discovered and fixed.

### Removed

- Support for python 2.

## Previous versions

See [CHANGELOG.old](CHANGELOG.old) for older versions.
