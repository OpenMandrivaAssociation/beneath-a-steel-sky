%define scummvmdir %{_datadir}/scummvm/

Name: beneath-a-steel-sky
Summary: A adventure game using scummvm
Version: 1.2
Release: 3
Source0: http://prdownloads.sourceforge.net/scummvm/bass-cd-%{version}.tar.bz2
Source1: bass-48.png
Source2: bass-32.png
Source3: bass-16.png
License: Freeware
Url:     http://scummvm.org
Group:   Games/Adventure
BuildRequires: unzip
Requires: scummvm
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A science-fiction thriller set in a bleak post-apocalyptic vision
of the future, Beneath a Steel Sky revolves around "Union City",
where selfishness, rivalry, and corruption by its citizens
seems to be all too common, those who can afford it live
underground, away from the pollution and social problems
which are plaguing the city. 

You take on the role of Robert Foster, an outcast of sorts
from the city since a boy who was raised in a remote environment
outside of Union City simply termed "the gap". Robert's mother
took him away from Union City as a child on their way to "Hobart"
but the helicopter crashed on its way, unfortunately Robert's 
mother dies, but he survives and is left to be raised by a 
local tribe from the gap. 

Years later, Union City security drops by and abducts
Robert, killing his tribe in the process; upon reaching
the city the helicopter taking him there crashes with
him escaping, high upon a tower block in the middle of the
city he sets out to discover the truth about his past,
and to seek vengeance for the killing of his tribe.

This game was released by Revolution studio to help the scummvm
project. However, this is not a free game ( free as freespeech ), even
if source code can be seen. That's why it belongs to the non-free repository.

%prep
%setup -q -n bass-cd-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{scummvmdir}/%{name}
cp sky* %{buildroot}/%{scummvmdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Beneath A Steel Sky
Comment=%{summary}
Exec=%{_gamesbindir}/scummvm -p%{scummvmdir}/%{name}  sky
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF
install -m 644 -D %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -m 644 -D %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 -D %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt
%{scummvmdir}/%{name}
%{_datadir}/applications/mandriva-*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

