%define upstream_name    Dist-Zilla-Plugin-Repository
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Automatically sets repository URL from svn/svk/Git checkout for Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildArch:	noarch

%description
The code is mostly a copy-paste of the Module::Install::Repository manpage

ATTRIBUTES
    * * git_remote

      This is the name of the remote to use for the public repository (if
      you use Git). By default, unsurprisingly, to _origin_.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Cannot find user config
#make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


