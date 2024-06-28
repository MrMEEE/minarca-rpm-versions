
%global python3_pkgversion 3.11

Name:           python-scikit-build
Version:        0.17.6
Release:        %autorelease
Summary:        Improved build system generator for Python C/C++/Fortran/Cython extensions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/scikit-build/scikit-build
Source:         %{pypi_source scikit_build}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scikit-build' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-scikit-build
Summary:        %{summary}

%description -n python%{python3_pkgversion}-scikit-build %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-scikit-build cov,docs,doctest,test


%prep
%autosetup -p1 -n scikit_build-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cov,docs,doctest,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-scikit-build -f %{pyproject_files}


%changelog
%autochangelog