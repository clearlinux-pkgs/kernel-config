Name:           kernel-config
Version:        3
Release:        19
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
Source10:        base-4.20
Source11:        mandatory-4.20
Source12:        base-5.0
Source13:        mandatory-5.0

%description

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
