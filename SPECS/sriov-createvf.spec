Summary: mellanox sriov-createvf service
Name: sriov-createvf
Version: 1
Release: 1
License: GPL
# BuildArch states the intented architecture; in this case we build a package for all.
# if you copy binaries for a specific architecture please state it here
BuildArch: noarch
Group: Development/Tools
BuildRoot: /tmp/sriov-createvf

%description
sriov-createvf service configuration files will be copied to the system

%prep

%build

%install
# Installing happens here, normally using the “make install”
# command, it normally places the files
# where they need to go. You can also copy the files, as we do here...

# First we make sure we start clean
rm -rf $RPM_BUILD_ROOT

# Then we create the directories where the files go
# don't worry if the directories exist on your target systems, rpm
# creates if necessary
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system/

# The actual moving
cp /root/rpmbuild/SOURCES/sriov-createvf/bin/sriov-createvf $RPM_BUILD_ROOT/bin
cp /root/rpmbuild/SOURCES/sriov-createvf/etc/sysconfig/sriov-createvf $RPM_BUILD_ROOT/etc/sysconfig/
cp /root/rpmbuild/SOURCES/sriov-createvf/etc/systemd/system/sriov-createvf.service $RPM_BUILD_ROOT/etc/systemd/system/

%files
# The file section, it has to be exact, matching all files.
# Here you have the power to implement all rights, even if they are different in the tar.gz
/bin/sriov-createvf
/etc/sysconfig/sriov-createvf
/etc/systemd/system/sriov-createvf.service

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 2 2017 Dany Kaufman <danyk@iguazio.com> - 1-1
Initial creation
