# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/listings
# catalog-date 2007-03-12 20:45:12 +0100
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-listings
Version:	1.4
Release:	1
Summary:	Typeset source code listings using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listings
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset programs (programming code) within LaTeX. The source
code is read directly by TeX. Keywords, comments and strings
can be typeset using different styles (default is bold for
keywords, italic for comments and no special style for
strings). Includes support for hyperref. To use, simply
\usepackage{listings}, identify the language with
\lstset{language=Python}, then employ the \begin{lstlisting}
... \end{lstlisting} environment or the
\lstinputlisting{filename.py} command. Short (in-line) listings
are also available, using either \lstinline|...| or | ... |
(after defining the | token with the \lstMakeShortInline
command).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listings/listings.cfg
%{_texmfdistdir}/tex/latex/listings/listings.sty
%{_texmfdistdir}/tex/latex/listings/lstdoc.sty
%{_texmfdistdir}/tex/latex/listings/lstlang1.sty
%{_texmfdistdir}/tex/latex/listings/lstlang2.sty
%{_texmfdistdir}/tex/latex/listings/lstlang3.sty
%{_texmfdistdir}/tex/latex/listings/lstmisc.sty
%doc %{_texmfdistdir}/doc/latex/listings/README
%doc %{_texmfdistdir}/doc/latex/listings/listings.pdf
#- source
%doc %{_texmfdistdir}/source/latex/listings/Makefile
%doc %{_texmfdistdir}/source/latex/listings/listings.dtx
%doc %{_texmfdistdir}/source/latex/listings/listings.ins
%doc %{_texmfdistdir}/source/latex/listings/lstdrvrs.dtx
%doc %{_texmfdistdir}/source/latex/listings/lstdrvrs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
