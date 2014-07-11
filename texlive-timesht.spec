# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-timesht
Version:	20111104
Release:	8
Summary:	TeXLive timesht package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timesht.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timesht.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timesht.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive timesht package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/timesht/timesht.cls
%doc %{_texmfdistdir}/doc/latex/timesht/README
%doc %{_texmfdistdir}/doc/latex/timesht/timesheet.tex
#- source
%doc %{_texmfdistdir}/source/latex/timesht/timesht.dtx
%doc %{_texmfdistdir}/source/latex/timesht/timesht.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756916
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719749
- texlive-timesht
- texlive-timesht
- texlive-timesht
- texlive-timesht

