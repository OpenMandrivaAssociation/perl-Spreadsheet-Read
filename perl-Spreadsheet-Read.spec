%define upstream_name    Spreadsheet-Read
%define upstream_version 0.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Transparent read the data from a spreadsheet
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Spreadsheet::ParseExcel)
BuildRequires: perl(Spreadsheet::ParseExcel::FmtDefault)
BuildRequires: perl(Spreadsheet::ReadSXC)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Text::CSV)
BuildRequires: perl(Text::CSV_PP)
BuildRequires: perl(Text::CSV_XS)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/*


