%define debug_package %{nil}

Summary: Supermicro Update Manager 2.0.0
Name: sum_2.0.0_Linux_x86_64_20170930
Version: 1
Release: 1
License: GPL
# BuildArch states the intented architecture; in this case we build a package for all.
# if you copy binaries for a specific architecture please state it here
BuildArch: x86_64
Group: Development/Tools
# The name of our source tar.gz file is next, make sure this name is correct. The version number
# does matter a lot!
Source: /root/rpmbuild/SOURCES/sum_2.0.0_Linux_x86_64_20170930.tar.gz
BuildRoot: /tmp/sum

%description
SuperMicro Update Manager files will be copied to the system

%prep
%setup -n sum_2.0.0_Linux_x86_64
# In the prep section the tar.gz file gets unpacked to a directory.

%build
# Normally this part would be full of fancy compile stuff. Make this, make that.
# We simple folks, we just want to copy some files out of a tar.gz.
# so we pass this section with nothing done...

%install
# Installing happens here, normally using the “make install”
# command, it normally places the files
# where they need to go. You can also copy the files, as we do here...

# First we make sure we start clean
rm -rf $RPM_BUILD_ROOT

# Then we create the directories where the files go
# don't worry if the directories exist on your target systems, rpm
# creates if necessary
mkdir -p $RPM_BUILD_ROOT/opt/sum

# The actual moving
cp -r * $RPM_BUILD_ROOT/opt/sum/

%files
# The file section, it has to be exact, matching all files.
# Here you have the power to implement all rights, even if they are different in the tar.gz
/opt/sum/ExternalData/SMCIPID.txt
/opt/sum/ExternalData/VENID.txt
/opt/sum/ReleaseNote.txt
/opt/sum/SUM_UserGuide.pdf
/opt/sum/driver/RHL4_x86_64/sum_bios.ko
/opt/sum/driver/RHL5_x86_64/sum_bios.ko
/opt/sum/driver/RHL6_x86_64/sum_bios.ko
/opt/sum/driver/RHL7_x86_64/sum_bios.ko
/opt/sum/sum

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 2 2017 Dany Kaufman <danyk@iguazio.com> - 1-1
Initial creation
