Name:     kcat
Version:  1.7.0
Release:  1%{?dist}
Summary:  kcat is a generic non-JVM producer and consumer for Apache Kafka, think of it as a netcat for Kafka.
Group:    Productivity/Networking/Other
License:  BSD-2-Clause
URL:      https://github.com/edenhill/kcat
Source:   kcat-%{version}.tar.gz
Requires: librdkafka1 avro-c confluent-libserdes yajl jansson

BuildRequires: make gcc-c++ >= 4.1 librdkafka-devel avro-c-devel confluent-libserdes-devel yajl-devel jansson-devel 
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
kcat is a generic non-JVM producer and consumer for Apache Kafka >= 0.8,
think of it as a netcat for Kafka.

In producer mode kcat reads messages from stdin, delimited with a
configurable delimeter (-D, defaults to newline), and produces them to the
provided Kafka cluster (-b), topic (-t) and partition (-p).

In consumer mode kcat reads messages from a topic and partition and prints
them to stdout using the configured message delimiter.

kcat also features a Metadata list (-L) mode to display the current state
of the Kafka cluster and its topics and partitions.

kcat is fast and lightweight; statically linked it is no more than 150Kb.

kcat was formerly known as kafkacat.

%prep
%setup -q

%configure

%build
make

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(755,root,root)
%{_bindir}/kcat
%defattr(644,root,root)
%doc README.md
%doc LICENSE

%changelog

* Mon Aug 31 2021 Piotr Smolinski <piotr.smolinski@cconfluent.io> 1.7.0
- Relase 1.7.0

* Wed Jun 03 2015 Magnus Edenhill <magnus@edenhill.se> 1.2.0-1
- Relase 1.2.0

* Fri Dec 19 2014 François Saint-Jacques <fsaintjacques@gmail.com> 1.1.0-1
- Initial RPM package
