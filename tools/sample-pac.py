"""
This sample PAC string demonstrates various common PAC file features:

Direct connections for local/internal IP ranges (10.x.x.x, 172.16.x.x, 192.168.x.x, 127.x.x.x)
Specific proxy routing for internal corporate domains
Blocking domains by routing to a black hole proxy
Protocol-based routing (different handling for HTTP vs HTTPS)
SOCKS proxy usage for specific sites
Failover proxies (multiple proxies with fallback to DIRECT)
Time-based load balancing between proxies

The PAC file uses standard PAC functions like:

isPlainHostName() - checks if hostname has no dots
shExpMatch() - shell expression matching (wildcards)
isInNet() - checks if IP is in a network range
dnsResolve() - resolves hostname to IP
dnsDomainIs() - checks if host is in a domain
dateRange() - checks date ranges

This should provide a good test case for your Python PAC parser with various routing rules and PAC functions to parse.
"""

pac = """function FindProxyForURL(url, host) {
    // If the hostname matches local addresses, go direct
    if (isPlainHostName(host) ||
        shExpMatch(host, "*.local") ||
        isInNet(dnsResolve(host), "10.0.0.0", "255.0.0.0") ||
        isInNet(dnsResolve(host), "172.16.0.0", "255.240.0.0") ||
        isInNet(dnsResolve(host), "192.168.0.0", "255.255.0.0") ||
        isInNet(dnsResolve(host), "127.0.0.0", "255.255.255.0")) {
        return "DIRECT";
    }

    // Use specific proxy for internal corporate domains
    if (dnsDomainIs(host, ".internal.company.com") ||
        dnsDomainIs(host, ".corp.example.com")) {
        return "PROXY internal-proxy.company.com:8080";
    }

    // Block certain domains
    if (shExpMatch(host, "*.blocked-site.com") ||
        shExpMatch(host, "*.ads.example.com")) {
        return "PROXY 127.0.0.1:9999";  // Black hole proxy
    }

    // Use different proxies based on protocol
    if (url.substring(0, 5) == "http:") {
        return "PROXY http-proxy.company.com:3128; DIRECT";
    }

    if (url.substring(0, 6) == "https:") {
        return "PROXY https-proxy.company.com:3129; PROXY backup-proxy.company.com:3128; DIRECT";
    }

    // Special handling for specific sites
    if (dnsDomainIs(host, ".youtube.com") ||
        dnsDomainIs(host, ".googlevideo.com")) {
        return "SOCKS5 socks-proxy.company.com:1080";
    }

    // Load balance between multiple proxies for general traffic
    if (dateRange("MON", "WED")) {
        return "PROXY proxy1.company.com:8080; PROXY proxy2.company.com:8080; DIRECT";
    } else {
        return "PROXY proxy2.company.com:8080; PROXY proxy1.company.com:8080; DIRECT";
    }
}"""
