Name:           kernel-config
Version:        1
Release:        5
License:        GPL-2.0
Summary:        Linux kernel configuration common fragments
Group:          kernel
Source0:        apply-kconfig
Source1:        base-4.14
Source2:        mandatory-4.14
Source3:        base-4.17
Source4:        mandatory-4.17
Source5:        base-4.18
Source6:        mandatory-4.18

%description

%description
Kernel configuration common fragments

%prep
mkdir -p configs
mkdir -p bin
cp %{SOURCE0} bin/
cp %{SOURCE1} configs/
cp %{SOURCE2} configs/
cp %{SOURCE3} configs/
cp %{SOURCE4} configs/
cp %{SOURCE5} configs/
cp %{SOURCE6} configs/

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
