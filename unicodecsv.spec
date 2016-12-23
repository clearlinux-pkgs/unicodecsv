#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unicodecsv
Version  : 0.14.1
Release  : 9
URL      : https://pypi.python.org/packages/source/u/unicodecsv/unicodecsv-0.14.1.tar.gz
Source0  : https://pypi.python.org/packages/source/u/unicodecsv/unicodecsv-0.14.1.tar.gz
Summary  : Python2's stdlib csv module is nice, but it doesn't support unicode. This module is a drop-in replacement which *does*.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: unicodecsv-python
BuildRequires : linecache2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testtools
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
unicodecsv
==========
The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.  Supported versions are python 2.7, 3.3, 3.4, 3.5, and pypy 2.4.0.

%package python
Summary: python components for the unicodecsv package.
Group: Default

%description python
python components for the unicodecsv package.


%prep
%setup -q -n unicodecsv-0.14.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
