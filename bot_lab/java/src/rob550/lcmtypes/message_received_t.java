/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package rob550.lcmtypes;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class message_received_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public long creation_time;
    public String channel;
 
    public message_received_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x8f572e30405376e3L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(rob550.lcmtypes.message_received_t.class))
            return 0L;
 
        classes.add(rob550.lcmtypes.message_received_t.class);
        long hash = LCM_FINGERPRINT_BASE
            ;
        classes.remove(classes.size() - 1);
        return (hash<<1) + ((hash>>63)&1);
    }
 
    public void encode(DataOutput outs) throws IOException
    {
        outs.writeLong(LCM_FINGERPRINT);
        _encodeRecursive(outs);
    }
 
    public void _encodeRecursive(DataOutput outs) throws IOException
    {
        char[] __strbuf = null;
        outs.writeLong(this.utime); 
 
        outs.writeLong(this.creation_time); 
 
        __strbuf = new char[this.channel.length()]; this.channel.getChars(0, this.channel.length(), __strbuf, 0); outs.writeInt(__strbuf.length+1); for (int _i = 0; _i < __strbuf.length; _i++) outs.write(__strbuf[_i]); outs.writeByte(0); 
 
    }
 
    public message_received_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public message_received_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static rob550.lcmtypes.message_received_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        rob550.lcmtypes.message_received_t o = new rob550.lcmtypes.message_received_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        char[] __strbuf = null;
        this.utime = ins.readLong();
 
        this.creation_time = ins.readLong();
 
        __strbuf = new char[ins.readInt()-1]; for (int _i = 0; _i < __strbuf.length; _i++) __strbuf[_i] = (char) (ins.readByte()&0xff); ins.readByte(); this.channel = new String(__strbuf);
 
    }
 
    public rob550.lcmtypes.message_received_t copy()
    {
        rob550.lcmtypes.message_received_t outobj = new rob550.lcmtypes.message_received_t();
        outobj.utime = this.utime;
 
        outobj.creation_time = this.creation_time;
 
        outobj.channel = this.channel;
 
        return outobj;
    }
 
}
