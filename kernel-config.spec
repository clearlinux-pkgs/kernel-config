Name:           kernel-config
Version:        5
Release:        65
License:        GPL-2.0
Summary:        Linux kernel configuration common fragments
Group:          kernel
Source0:        apply-kconfig
Source1:        update-fragment
Source2:        base-4.14
Source3:        mandatory-4.14
Source4:        base-4.17
Source5:        mandatory-4.17
Source6:        base-4.18
Source7:        mandatory-4.18
Source8:        base-4.19
Source9:        mandatory-4.19
Source10:       base-4.20
Source11:       mandatory-4.20
Source12:       base-5.0
Source13:       mandatory-5.0
Source14:       base-5.1
Source15:       mandatory-5.1
Source16:       base-5.2
Source17:       mandatory-5.2
Source18:       base-5.3
Source19:       mandatory-5.3
Source20:       base-5.4
Source21:       mandatory-5.4
Source22:       base-5.5
Source23:       mandatory-5.5
Source24:       base-5.6
Source25:       mandatory-5.6
Source26:       base-5.7
Source27:       mandatory-5.7
Source28:       base-5.8
Source29:       mandatory-5.8
Source30:       base-5.9
Source31:       mandatory-5.9
Source32:       base-5.10
Source33:       mandatory-5.10
Source34:       base-5.12
Source35:       mandatory-5.12
Source36:       base-5.13
Source37:       mandatory-5.13
Source38:       base-5.14
Source39:       mandatory-5.14
Source40:       base-5.15
Source41:       mandatory-5.15
Source42:       base-5.16
Source43:       mandatory-5.16
Source44:       base-5.17
Source45:       mandatory-5.17
Source46:       base-5.18
Source47:       mandatory-5.18
Source48:       base-5.19
Source49:       mandatory-5.19
Source50:       base-6.0
Source51:       mandatory-6.0
Source52:       base-6.1
Source53:       mandatory-6.1
Source54:       base-6.2
Source55:       mandatory-6.2
Source56:       base-6.3
Source57:       mandatory-6.3

%description
Kernel configuration common fragments

%prep
mkdir -p configs
mkdir -p bin
cp %{SOURCE0} bin/
cp %{SOURCE1} bin/
cp %{SOURCE2} configs/
cp %{SOURCE3} configs/
cp %{SOURCE4} configs/
cp %{SOURCE5} configs/
cp %{SOURCE6} configs/
cp %{SOURCE7} configs/
cp %{SOURCE8} configs/
cp %{SOURCE9} configs/
cp %{SOURCE10} configs/
cp %{SOURCE11} configs/
cp %{SOURCE12} configs/
cp %{SOURCE13} configs/
cp %{SOURCE14} configs/
cp %{SOURCE15} configs/
cp %{SOURCE16} configs/
cp %{SOURCE17} configs/
cp %{SOURCE18} configs/
cp %{SOURCE19} configs/
cp %{SOURCE20} configs/
cp %{SOURCE21} configs/
cp %{SOURCE22} configs/
cp %{SOURCE23} configs/
cp %{SOURCE24} configs/
cp %{SOURCE25} configs/
cp %{SOURCE26} configs/
cp %{SOURCE27} configs/
cp %{SOURCE28} configs/
cp %{SOURCE29} configs/
cp %{SOURCE30} configs/
cp %{SOURCE31} configs/
cp %{SOURCE32} configs/
cp %{SOURCE33} configs/
cp %{SOURCE34} configs/
cp %{SOURCE35} configs/
cp %{SOURCE36} configs/
cp %{SOURCE37} configs/
cp %{SOURCE38} configs/
cp %{SOURCE39} configs/
cp %{SOURCE40} configs/
cp %{SOURCE41} configs/
cp %{SOURCE42} configs/
cp %{SOURCE43} configs/
cp %{SOURCE44} configs/
cp %{SOURCE45} configs/
cp %{SOURCE46} configs/
cp %{SOURCE47} configs/
cp %{SOURCE48} configs/
cp %{SOURCE49} configs/
cp %{SOURCE50} configs/
cp %{SOURCE51} configs/
cp %{SOURCE52} configs/
cp %{SOURCE53} configs/
cp %{SOURCE54} configs/
cp %{SOURCE55} configs/
cp %{SOURCE56} configs/
cp %{SOURCE57} configs/
cp %{SOURCE56} configs/base-6.4
cp %{SOURCE57} configs/mandatory-6.4
cp %{SOURCE56} configs/base-6.5
cp %{SOURCE57} configs/mandatory-6.5
cp %{SOURCE56} configs/base-6.6
cp %{SOURCE57} configs/mandatory-6.6
cp %{SOURCE56} configs/base-6.7
cp %{SOURCE57} configs/mandatory-6.7
cp %{SOURCE56} configs/base-6.8
cp %{SOURCE57} configs/mandatory-6.8

%build

%install
install -m 0755 -Dt %{buildroot}/usr/bin/ bin/*
install -m 0644 -Dt %{buildroot}/usr/share/kernel-config configs/*
for file in %{buildroot}/usr/share/kernel-config/*; do
  echo "# FILEVER=${file#%{buildroot}}-%{version}-%{release}">> $file
done

%files
%dir /usr/share/kernel-config
/usr/bin/*
/usr/share/kernel-config/*
