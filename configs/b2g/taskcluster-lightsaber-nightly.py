#!/usr/bin/env python
import os.path
config = {
    "default_vcs": "tc-vcs",
    "default_actions": [
        'checkout-sources',
        'checkout-lightsaber',
        'build',
        'make-updates',
        'prep-upload',
        'submit-to-balrog'
    ],
    "balrog_credentials_file": "balrog_credentials",
    "nightly_build": True,
    "env": {
        "GAIA_OPTIMIZE": "1",
        "B2G_UPDATER": "1",
        "B2G_UPDATE_CHANNEL": "cypress",
        "LIGHTSABER": "1",
        "BOWER_FLAGS": "--allow-root",
        "B2G_PATH": "%(work_dir)s",
        "WGET_OPTS": "-c -q"
    },
    "is_automation": True,
    "repo_remote_mappings": {
        'https://android.googlesource.com/': 'https://git.mozilla.org/external/aosp',
        'git://codeaurora.org/': 'https://git.mozilla.org/external/caf',
        'https://git.mozilla.org/b2g': 'https://git.mozilla.org/b2g',
        'git://github.com/mozilla-b2g/': 'https://git.mozilla.org/b2g',
        'git://github.com/mozilla/': 'https://git.mozilla.org/b2g',
        'https://git.mozilla.org/releases': 'https://git.mozilla.org/releases',
        'http://android.git.linaro.org/git-ro/': 'https://git.mozilla.org/external/linaro',
        'git://github.com/apitrace/': 'https://git.mozilla.org/external/apitrace',
    },
}
