
#ifdef QFILESIGLIB_EXPORTS
#define QFILESIGLIB_API extern "C" __declspec(dllexport)
#else
#define QFILESIGLIB_API __declspec(dllimport)
#endif

QFILESIGLIB_API BOOL GetAuthSignTimeW(__in_z WCHAR* szFile, __out WCHAR* szTimeStr,__in int nTimeLen);

QFILESIGLIB_API BOOL GetAuthSignIssuerNameW(__in_z LPCWSTR szFile, __inout_ecount_z(dwSizeInWords) LPWSTR lpNameBuf, __in DWORD dwSizeInWords);

QFILESIGLIB_API BOOL GetAuthSignOwnerNameW(__in_z LPCWSTR szFile, __inout_ecount_z(dwSizeInWords) LPWSTR lpNameBuf, __in DWORD dwSizeInWords);

QFILESIGLIB_API BOOL IsAuthSignValidW( __in_z LPCWSTR szFile );