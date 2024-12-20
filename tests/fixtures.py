import shutil
import sys
from collections.abc import Generator
from io import StringIO
from pathlib import Path
from typing import Any

import pytest
from sphinx.testing.util import SphinxTestApp


def copy_srcdir_to_tmpdir(srcdir, tmp):
    srcdir = Path(__file__).parent.resolve() / srcdir
    tmproot = tmp / Path(srcdir).name
    shutil.copytree(srcdir, tmproot, dirs_exist_ok=True)
    return tmproot


# Copied and slightly modified from `sphinx.testing.fixtures`.
@pytest.fixture(scope="module")
def do_app() -> Generator:
    """
    Provides make_app function to initialize SphinxTestApp instance.
    if you want to initialize 'app' in your test function. please use this
    instead of using SphinxTestApp class directory.
    """
    apps = []
    syspath = sys.path[:]

    def make(*args, **kwargs):
        status, warning = StringIO(), StringIO()
        kwargs.setdefault("status", status)
        kwargs.setdefault("warning", warning)
        app_: Any = SphinxTestApp(*args, **kwargs)
        apps.append(app_)
        return app_

    yield make

    sys.path[:] = syspath
    for app_ in reversed(apps):  # clean up applications from the new ones
        app_.cleanup()


@pytest.fixture(scope="module")
def test_app(do_app, sphinx_test_tempdir) -> Generator:
    test_tmp_dirs = ["_build", "_static", "_templates"]

    def _test_app(**builder_params):
        # Copy test srcdir to test temporary directory sphinx_test_tempdir.
        src_dir = copy_srcdir_to_tmpdir(
            builder_params["srcdir"], sphinx_test_tempdir
        )

        _app = do_app(
            srcdir=src_dir,
            buildername=builder_params.get("buildername", "html"),
            freshenv=builder_params.get("freshenv", None),
            confoverrides=builder_params.get("confoverrides", None),
            status=builder_params.get("status", None),
            warning=builder_params.get("warning", None),
            tags=builder_params.get("tags", None),
            docutilsconf=builder_params.get("docutilsconf", None),
            parallel=builder_params.get("parallel", 0),
        )
        test_tmp_dirs.append(sphinx_test_tempdir)
        _app.build()
        return _app

    yield _test_app

    for test_tmp_dir in reversed(test_tmp_dirs):
        shutil.rmtree(test_tmp_dir, True)


# ---------------------------------------------------------------------
# Fixtures for each sample project.

# There is no fixture for sample_prj_1 because it should not build
# successfully. It is just to test that the extension validates that
# the value provided in csi_default_color_scheme is a member of the
# list of color schemes provided in csi_color_schemes.


@pytest.fixture(scope="module")
def sample_prj2(test_app):
    """
    Sample Prj 2 uses directives ``cs_image`` and ``cs_figure``.

    It specifically includes 2 pages. The 1st page includes sphinx'
    directives ``image`` and ``figure``. The 2nd page includes ``cs_image`` and
    ``cs_figure`` directives, and the 3rd page includes a combination of all.
    """
    return test_app(buildername="html", srcdir="sample_prj_2")


@pytest.fixture(scope="module")
def sample_prj3(test_app):
    """
    Sample Prj 3 uses directives ``cs_image`` and ``cs_figure``.

    It has images with the language code in their name. It is a single page
    project that includes several images and figures with different URIs.
    """
    return test_app(buildername="html", srcdir="sample_prj_3")
