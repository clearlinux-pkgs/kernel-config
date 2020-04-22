Name:           kernel-config
Version:        4
Release:        44
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
