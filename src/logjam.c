#include <stdio.h>
#include <stdarg.h>

#include "../../afunix/src/client.h"

#ifdef TARGET_OS_WINDOWS
#define EXPORTABLE __declspec(dllexport)
#define LOGGER_ENDPOINT "C:\\tmp\\LOGGER"
#else
#define EXPORTABLE __attribute__((visibility("default")))
#define LOGGER_ENDPOINT "/tmp/LOGGER"
#endif


void BinToHex(const unsigned char* buff, int length, char* output, int outLength) {
	char binHex[] = "0123456789ABCDEF";

	if (!output || outLength < 4) return;
    if (!buff || length <= 0 || outLength <= 2 * length) return;

	*output = '\0';

	for (; length > 0; --length, outLength -= 2){
		unsigned char byte = *buff++;
		*output++ = binHex[(byte >> 4) & 0x0F];
		*output++ = binHex[byte & 0x0F];
	}
	if (outLength-- <= 0) return;
	*output++ = '\0';
}


EXPORTABLE int LogMessage(const char* fmt,...){
    char s[4096] = { 0x00 };
    va_list args;
    va_start(args, fmt);
    vsnprintf(s, sizeof(s) - 1, fmt, args);
    va_end(args);
    s[sizeof(s) - 1] = 0x00;
    return SendMsg(LOGGER_ENDPOINT,s);
}

EXPORTABLE int LogBuffer(unsigned char* buffer, unsigned int length){
    char s[4096] = {0x00};
    BinToHex(buffer,length,s,sizeof(s));
    return SendMsg(LOGGER_ENDPOINT,s);
}