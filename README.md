# reproj

Reproject shapely features

[![build badge](https://github.com/sgoodm/python-reproj/actions/workflows/test-with-coverage.yml/badge.svg)](https://github.com/sgoodm/python-reproj/actions/workflows/test-and-coverage.yml)
[![Coverage Status](https://coveralls.io/repos/github/sgoodm/python-reproj/badge.svg)](https://coveralls.io/github/sgoodm/python-reproj)
[![Downloads](https://static.pepy.tech/personalized-badge/distancerasters?period=total&units=international_system&left_color=lightgrey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/distancerasters)


Reproj is a minimalistic package designed to do one thing: reproject shapely features with a single call. GeoPandas has a simple `to_crs` method for GeoDataFrames which we aim to mirror in ease of use for standalone shapely features. To be honest, this isn't difficult to do using pyproj and shapely with a couple of lines of code, but we decided to make it even easier.

Without reproj, you would use the following:
``` python

import pyproj
import shapely.ops

new_transformer = pyproj.Transformer.from_crs(4326, 32630)
utm_shape = shapely.ops.transform(new_transformer.transform, wgs84_shape)

```

With reproj, all you need is:
``` python
from reproj import reproj

utm_shape = reproj(wgs84_shape, 4326, 32630)

```

To see other practical ways of using  `reproj` for your application, check out the [examples](examples).


## Installation


### Using pip

The latest version of reproj is [available on PyPi](https://pypi.org/project/reproj/), and can be installed with Pip:
```sh
pip install reproj
```

If you'd like to install the latest development (alpha) release, there may be a newer version on [TestPyPi](https://test.pypi.org/project/reproj/):
```sh
pip install -i https://test.pypi.org/simple/ reproj
```

### From source

To install this package from source, first clone this repository, then use pip to install:
```sh
git clone git@github.com:sgoodm/python-reproj.git
cd python-reproj
pip install .
```



## Contribute

New issues are always welcome, and if you'd like to make a change, fork the repo and submit a pull request.


### Testing and Coverage

We use Pytest and Coveralls to run unit tests and track code coverage of tests. If you submit code, please make sure it passes existing tests and adds relevant testing coverage for new features.

You can run tests and coverage checks locally, or you can fork the repository and utilize GitHub actions and Coveralls. To use GitHub actions and Coveralls, you'll need to add your forked repo to your own Coverall accounts and add you Coveralls token to your repository as a GitHub Secret (see below).


To run tests and coverage checks locally, you can use the following commands:
```sh
pip install pytest coverage
coverage run -m pytest ./
coverage html
```

### GitHub Secrets

There are three GitHub Secrets required to enable all of our GitHub Actions:
1. COVERALLS_REPO_TOKEN - this is the API token for Coveralls, used for publishing code coverage reports
2. TEST_PYPI_API_TOKEN - this is the API token for TestPyPi, needed for publishing alpha releases
3. PYPI_API_TOKEN - this is the API token for PyPi, needed for publishing releases

Note: contributors do not need PyPi tokens; if you create a new release in a forked repo it will trigger a GitHub action that will attempt to publish to PyPi and fail.
