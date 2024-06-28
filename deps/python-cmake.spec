
%global python3_pkgversion 3.11

Name:           python-cmake
Version:        3.29.6
Release:        %autorelease
Summary:        CMake is an open-source, cross-platform family of tools designed to build, test and package software

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://cmake.org
Source:         %{pypi_source cmake}

BuildArch:      x86_64

BuildRequires:  python%{python3_pkgversion}-devel cmake ninja-build gcc gcc-c++ openssl-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cmake' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cmake
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cmake %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n cmake-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cmake -f %{pyproject_files}


%changelog
%autochangelog
