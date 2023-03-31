Name:		texlive-listings
Version:	55265
Release:	2
Summary:	Typeset source code listings using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listings
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to typeset programs (programming
code) within LaTeX; the source code is read directly by TeX--no
front-end processor is needed. Keywords, comments and strings
can be typeset using different styles (default is bold for
keywords, italic for comments and no special style for
strings). Support for hyperref is provided. To use,
\usepackage{listings}, identify the language of the object to
typeset, using a construct like: \lstset{language=Python}, then
use environment lstlisting for inline code. External files may
be formatted using \lstinputlisting to process a given file in
the form appropriate for the current language. Short (in-line)
listings are also available, using either \lstinline|...| or
|...| (after defining the | token with the \lstMakeShortInline
command).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listings
%doc %{_texmfdistdir}/doc/latex/listings
#- source
%doc %{_texmfdistdir}/source/latex/listings

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
