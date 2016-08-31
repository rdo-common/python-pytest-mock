%global pypi_name pytest-mock
%global file_name pytest_mock
%global desc This plugin installs a mocker fixture which is a thin-wrapper around the \
patching API provided by the mock package, but with the benefit of not having \
to worry about undoing patches at the end of a test.


Name:           python-%{pypi_name}
Version:        1.1
Release:        3%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-mock
Source0:        https://pypi.python.org/packages/99/0e/45906c1e876b175cb51d8710075be900948f44a5f6a92c90095bdcd846c8/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%description
%{desc}


%package -n     python2-%{pypi_name}
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-pytest >= 2.7
BuildRequires:  python2-mock
Requires:       python2-pytest >= 2.7
Requires:       python2-mock
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
Requires:       python3-pytest >= 2.7
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info

# Correct end of line encoding for README
sed -i 's/\r$//' README.rst


%build
%py2_build
%py3_build


%install
%py3_install
%py2_install


%check
PYTHONPATH="$(pwd)" py.test-%{python2_version} test_pytest_mock.py
PYTHONPATH="$(pwd)" py.test-%{python3_version} test_pytest_mock.py


%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{file_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/%{file_name}.py*


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}.py*
%{python3_sitelib}/__pycache__/%{file_name}*.py*


%changelog
* Wed Aug 31 2016 Julien Enselme <jujens@jujens.eu> - 1.1-3
- Use %%summary instead of custom %%sum macro

* Mon Aug 29 2016 Julien Enselme <jujens@jujens.eu> - 1.1-2
- Add python2-mock to BR so %%check passes correctly.

* Tue Jul 26 2016 Julien Enselme <jujens@jujens.eu> - 1.1-1
- Inital package
