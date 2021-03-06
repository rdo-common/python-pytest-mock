%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name pytest-mock
%global file_name pytest_mock
%global desc This plugin installs a mocker fixture which is a thin-wrapper around the \
patching API provided by the mock package, but with the benefit of not having \
to worry about undoing patches at the end of a test.


Name:           python-%{pypi_name}
Version:        1.6.0
Release:        2%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-mock
Source0:        https://pypi.python.org/packages/59/2a/18c5a08809b6383e6b1026d0307fa49f8eac1eaf9657bcd3446c7822cffd/pytest-mock-1.6.0.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python2-%{pypi_name}
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-pytest >= 2.7
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools_scm
BuildRequires:  python-setuptools
Requires:       python2-pytest >= 2.7
Requires:       python2-mock
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
BuildRequires:  python3-setuptools_scm
Requires:       python3-pytest >= 2.7
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}
%endif


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info

# Correct end of line encoding for README
sed -i 's/\r$//' README.rst


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install


%check
PYTHONPATH="$(pwd)" py.test-%{python2_version} test_pytest_mock.py
%if 0%{?with_python3}
PYTHONPATH="$(pwd)" py.test-%{python3_version} test_pytest_mock.py
%endif


%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{file_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/%{file_name}.py*
%{python2_sitelib}/_pytest_mock_version.py*


%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}.py*
%{python3_sitelib}/__pycache__/%{file_name}*.py*
%{python3_sitelib}/_pytest_mock_version.py*
%{python3_sitelib}/__pycache__/_pytest_mock_version.cpython*
%endif


%changelog
* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-2
- Add missing BR

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-1
- Update to 1.6.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-3
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 1.2-2
- Add patch to fix tests with pytest3

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 1.2-1
- Update to 1.2

* Wed Aug 31 2016 Julien Enselme <jujens@jujens.eu> - 1.1-3
- Use %%summary instead of custom %%sum macro

* Mon Aug 29 2016 Julien Enselme <jujens@jujens.eu> - 1.1-2
- Add python2-mock to BR so %%check passes correctly.

* Tue Jul 26 2016 Julien Enselme <jujens@jujens.eu> - 1.1-1
- Inital package
