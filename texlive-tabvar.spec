# revision 25665
# category Package
# catalog-ctan /macros/latex/contrib/tabvar
# catalog-date 2012-03-16 09:54:35 +0100
# catalog-license lppl1.3
# catalog-version 1.61
Name:		texlive-tabvar
Version:	1.61
Release:	1
Summary:	Typesetting tables showing variations of functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabvar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package is meant to ease the typesetting of tables
showing variations of functions as they are used in France.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/tabvar/tabvar.afm
%{_texmfdistdir}/fonts/map/dvips/tabvar/tabvar.map
%{_texmfdistdir}/fonts/tfm/public/tabvar/tabvar.tfm
%{_texmfdistdir}/fonts/type1/public/tabvar/tabvar.pfb
%{_texmfdistdir}/metapost/tabvar/tabvar.mp
%{_texmfdistdir}/tex/latex/tabvar/tabvar.1
%{_texmfdistdir}/tex/latex/tabvar/tabvar.2
%{_texmfdistdir}/tex/latex/tabvar/tabvar.3
%{_texmfdistdir}/tex/latex/tabvar/tabvar.cfg
%{_texmfdistdir}/tex/latex/tabvar/tabvar.sty
%doc %{_texmfdistdir}/doc/latex/tabvar/README
%doc %{_texmfdistdir}/doc/latex/tabvar/demo.pdf
%doc %{_texmfdistdir}/doc/latex/tabvar/demo.tex
%doc %{_texmfdistdir}/doc/latex/tabvar/tabvar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabvar/tabvar.dtx
%doc %{_texmfdistdir}/source/latex/tabvar/tabvar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.61-1
+ Revision: 787781
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 756506
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719650
- texlive-tabvar
- texlive-tabvar
- texlive-tabvar

