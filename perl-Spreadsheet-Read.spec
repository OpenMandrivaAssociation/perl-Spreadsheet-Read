%define upstream_name    Spreadsheet-Read
%define upstream_version 0.49

%if %{_use_internal_dependency_generator}
%define __noautoreq '/pro/bin/perl'
%else
%define _requires_exceptions /pro/bin/perl
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.49
Release:	1

Summary:	Transparent read the data from a spreadsheet
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Spreadsheet/Spreadsheet-Read-0.49.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Spreadsheet::ParseExcel)
BuildRequires:	perl(Spreadsheet::ParseExcel::FmtDefault)
BuildRequires:	perl(Spreadsheet::ReadSXC)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Text::CSV)
BuildRequires:	perl(Text::CSV_PP)
BuildRequires:	perl(Text::CSV_XS)

BuildArch:	noarch

%description
Spreadsheet::Read tries to transparently read *any* spreadsheet and return
its content in a universal manner independent of the parsing module that
does the actual spreadsheet scanning.

For OpenOffice this module uses Spreadsheet::ReadSXC

For Microsoft Excel this module uses Spreadsheet::ParseExcel or
Spreadsheet::XLSX

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.410.0-2mdv2011.0
+ Revision: 656965
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 596646
- update to 0.41

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 551200
- update to 0.40

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-2mdv2010.1
+ Revision: 536954
- remove unwanted shebang prereq

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 521764
- import perl-Spreadsheet-Read


* Tue Mar 16 2010 cpan2dist 0.38-1mdv
- initial mdv release, generated with cpan2dist

