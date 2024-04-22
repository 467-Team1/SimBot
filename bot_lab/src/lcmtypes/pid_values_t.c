// THIS IS AN AUTOMATICALLY GENERATED FILE.  DO NOT MODIFY
// BY HAND!!
//
// Generated by lcm-gen

#include <string.h>
#include "pid_values_t.h"

static int __pid_values_t_hash_computed;
static uint64_t __pid_values_t_hash;

uint64_t __pid_values_t_hash_recursive(const __lcm_hash_ptr *p)
{
    const __lcm_hash_ptr *fp;
    for (fp = p; fp != NULL; fp = fp->parent)
        if (fp->v == __pid_values_t_get_hash)
            return 0;

    __lcm_hash_ptr cp;
    cp.parent =  p;
    cp.v = __pid_values_t_get_hash;
    (void) cp;

    uint64_t hash = (uint64_t)0xbdbad1235b5e51cdLL
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
        ;

    return (hash<<1) + ((hash>>63)&1);
}

int64_t __pid_values_t_get_hash(void)
{
    if (!__pid_values_t_hash_computed) {
        __pid_values_t_hash = (int64_t)__pid_values_t_hash_recursive(NULL);
        __pid_values_t_hash_computed = 1;
    }

    return __pid_values_t_hash;
}

int __pid_values_t_encode_array(void *buf, int offset, int maxlen, const pid_values_t *p, int elements)
{
    int pos = 0, element;
    int thislen;

    for (element = 0; element < elements; element++) {

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

    }
    return pos;
}

int pid_values_t_encode(void *buf, int offset, int maxlen, const pid_values_t *p)
{
    int pos = 0, thislen;
    int64_t hash = __pid_values_t_get_hash();

    thislen = __int64_t_encode_array(buf, offset + pos, maxlen - pos, &hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    thislen = __pid_values_t_encode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

int __pid_values_t_encoded_array_size(const pid_values_t *p, int elements)
{
    int size = 0, element;
    for (element = 0; element < elements; element++) {

        size += __float_encoded_array_size(&(p[element].motor_a_kp), 1);

        size += __float_encoded_array_size(&(p[element].motor_a_ki), 1);

        size += __float_encoded_array_size(&(p[element].motor_a_kd), 1);

        size += __float_encoded_array_size(&(p[element].motor_a_Tf), 1);

        size += __float_encoded_array_size(&(p[element].motor_b_kp), 1);

        size += __float_encoded_array_size(&(p[element].motor_b_ki), 1);

        size += __float_encoded_array_size(&(p[element].motor_b_kd), 1);

        size += __float_encoded_array_size(&(p[element].motor_b_Tf), 1);

        size += __float_encoded_array_size(&(p[element].motor_c_kp), 1);

        size += __float_encoded_array_size(&(p[element].motor_c_ki), 1);

        size += __float_encoded_array_size(&(p[element].motor_c_kd), 1);

        size += __float_encoded_array_size(&(p[element].motor_c_Tf), 1);

        size += __float_encoded_array_size(&(p[element].bf_trans_kp), 1);

        size += __float_encoded_array_size(&(p[element].bf_trans_ki), 1);

        size += __float_encoded_array_size(&(p[element].bf_trans_kd), 1);

        size += __float_encoded_array_size(&(p[element].bf_trans_Tf), 1);

        size += __float_encoded_array_size(&(p[element].bf_rot_kp), 1);

        size += __float_encoded_array_size(&(p[element].bf_rot_ki), 1);

        size += __float_encoded_array_size(&(p[element].bf_rot_kd), 1);

        size += __float_encoded_array_size(&(p[element].bf_rot_Tf), 1);

    }
    return size;
}

int pid_values_t_encoded_size(const pid_values_t *p)
{
    return 8 + __pid_values_t_encoded_array_size(p, 1);
}

size_t pid_values_t_struct_size(void)
{
    return sizeof(pid_values_t);
}

int pid_values_t_num_fields(void)
{
    return 20;
}

int pid_values_t_get_field(const pid_values_t *p, int i, lcm_field_t *f)
{
    if (0 > i || i >= pid_values_t_num_fields())
        return 1;
    
    switch (i) {
    
        case 0: {
            f->name = "motor_a_kp";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_a_kp;
            return 0;
        }
        
        case 1: {
            f->name = "motor_a_ki";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_a_ki;
            return 0;
        }
        
        case 2: {
            f->name = "motor_a_kd";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_a_kd;
            return 0;
        }
        
        case 3: {
            f->name = "motor_a_Tf";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_a_Tf;
            return 0;
        }
        
        case 4: {
            f->name = "motor_b_kp";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_b_kp;
            return 0;
        }
        
        case 5: {
            f->name = "motor_b_ki";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_b_ki;
            return 0;
        }
        
        case 6: {
            f->name = "motor_b_kd";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_b_kd;
            return 0;
        }
        
        case 7: {
            f->name = "motor_b_Tf";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_b_Tf;
            return 0;
        }
        
        case 8: {
            f->name = "motor_c_kp";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_c_kp;
            return 0;
        }
        
        case 9: {
            f->name = "motor_c_ki";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_c_ki;
            return 0;
        }
        
        case 10: {
            f->name = "motor_c_kd";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_c_kd;
            return 0;
        }
        
        case 11: {
            f->name = "motor_c_Tf";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->motor_c_Tf;
            return 0;
        }
        
        case 12: {
            f->name = "bf_trans_kp";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_trans_kp;
            return 0;
        }
        
        case 13: {
            f->name = "bf_trans_ki";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_trans_ki;
            return 0;
        }
        
        case 14: {
            f->name = "bf_trans_kd";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_trans_kd;
            return 0;
        }
        
        case 15: {
            f->name = "bf_trans_Tf";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_trans_Tf;
            return 0;
        }
        
        case 16: {
            f->name = "bf_rot_kp";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_rot_kp;
            return 0;
        }
        
        case 17: {
            f->name = "bf_rot_ki";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_rot_ki;
            return 0;
        }
        
        case 18: {
            f->name = "bf_rot_kd";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_rot_kd;
            return 0;
        }
        
        case 19: {
            f->name = "bf_rot_Tf";
            f->type = LCM_FIELD_FLOAT;
            f->typestr = "float";
            f->num_dim = 0;
            f->data = (void *) &p->bf_rot_Tf;
            return 0;
        }
        
        default:
            return 1;
    }
}

const lcm_type_info_t *pid_values_t_get_type_info(void)
{
    static int init = 0;
    static lcm_type_info_t typeinfo;
    if (!init) {
        typeinfo.encode         = (lcm_encode_t) pid_values_t_encode;
        typeinfo.decode         = (lcm_decode_t) pid_values_t_decode;
        typeinfo.decode_cleanup = (lcm_decode_cleanup_t) pid_values_t_decode_cleanup;
        typeinfo.encoded_size   = (lcm_encoded_size_t) pid_values_t_encoded_size;
        typeinfo.struct_size    = (lcm_struct_size_t)  pid_values_t_struct_size;
        typeinfo.num_fields     = (lcm_num_fields_t) pid_values_t_num_fields;
        typeinfo.get_field      = (lcm_get_field_t) pid_values_t_get_field;
        typeinfo.get_hash       = (lcm_get_hash_t) __pid_values_t_get_hash;
    }
    
    return &typeinfo;
}
int __pid_values_t_decode_array(const void *buf, int offset, int maxlen, pid_values_t *p, int elements)
{
    int pos = 0, thislen, element;

    for (element = 0; element < elements; element++) {

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_a_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_b_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].motor_c_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_trans_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_kp), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_ki), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_kd), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, &(p[element].bf_rot_Tf), 1);
        if (thislen < 0) return thislen; else pos += thislen;

    }
    return pos;
}

int __pid_values_t_decode_array_cleanup(pid_values_t *p, int elements)
{
    int element;
    for (element = 0; element < elements; element++) {

        __float_decode_array_cleanup(&(p[element].motor_a_kp), 1);

        __float_decode_array_cleanup(&(p[element].motor_a_ki), 1);

        __float_decode_array_cleanup(&(p[element].motor_a_kd), 1);

        __float_decode_array_cleanup(&(p[element].motor_a_Tf), 1);

        __float_decode_array_cleanup(&(p[element].motor_b_kp), 1);

        __float_decode_array_cleanup(&(p[element].motor_b_ki), 1);

        __float_decode_array_cleanup(&(p[element].motor_b_kd), 1);

        __float_decode_array_cleanup(&(p[element].motor_b_Tf), 1);

        __float_decode_array_cleanup(&(p[element].motor_c_kp), 1);

        __float_decode_array_cleanup(&(p[element].motor_c_ki), 1);

        __float_decode_array_cleanup(&(p[element].motor_c_kd), 1);

        __float_decode_array_cleanup(&(p[element].motor_c_Tf), 1);

        __float_decode_array_cleanup(&(p[element].bf_trans_kp), 1);

        __float_decode_array_cleanup(&(p[element].bf_trans_ki), 1);

        __float_decode_array_cleanup(&(p[element].bf_trans_kd), 1);

        __float_decode_array_cleanup(&(p[element].bf_trans_Tf), 1);

        __float_decode_array_cleanup(&(p[element].bf_rot_kp), 1);

        __float_decode_array_cleanup(&(p[element].bf_rot_ki), 1);

        __float_decode_array_cleanup(&(p[element].bf_rot_kd), 1);

        __float_decode_array_cleanup(&(p[element].bf_rot_Tf), 1);

    }
    return 0;
}

int pid_values_t_decode(const void *buf, int offset, int maxlen, pid_values_t *p)
{
    int pos = 0, thislen;
    int64_t hash = __pid_values_t_get_hash();

    int64_t this_hash;
    thislen = __int64_t_decode_array(buf, offset + pos, maxlen - pos, &this_hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;
    if (this_hash != hash) return -1;

    thislen = __pid_values_t_decode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

int pid_values_t_decode_cleanup(pid_values_t *p)
{
    return __pid_values_t_decode_array_cleanup(p, 1);
}

int __pid_values_t_clone_array(const pid_values_t *p, pid_values_t *q, int elements)
{
    int element;
    for (element = 0; element < elements; element++) {

        __float_clone_array(&(p[element].motor_a_kp), &(q[element].motor_a_kp), 1);

        __float_clone_array(&(p[element].motor_a_ki), &(q[element].motor_a_ki), 1);

        __float_clone_array(&(p[element].motor_a_kd), &(q[element].motor_a_kd), 1);

        __float_clone_array(&(p[element].motor_a_Tf), &(q[element].motor_a_Tf), 1);

        __float_clone_array(&(p[element].motor_b_kp), &(q[element].motor_b_kp), 1);

        __float_clone_array(&(p[element].motor_b_ki), &(q[element].motor_b_ki), 1);

        __float_clone_array(&(p[element].motor_b_kd), &(q[element].motor_b_kd), 1);

        __float_clone_array(&(p[element].motor_b_Tf), &(q[element].motor_b_Tf), 1);

        __float_clone_array(&(p[element].motor_c_kp), &(q[element].motor_c_kp), 1);

        __float_clone_array(&(p[element].motor_c_ki), &(q[element].motor_c_ki), 1);

        __float_clone_array(&(p[element].motor_c_kd), &(q[element].motor_c_kd), 1);

        __float_clone_array(&(p[element].motor_c_Tf), &(q[element].motor_c_Tf), 1);

        __float_clone_array(&(p[element].bf_trans_kp), &(q[element].bf_trans_kp), 1);

        __float_clone_array(&(p[element].bf_trans_ki), &(q[element].bf_trans_ki), 1);

        __float_clone_array(&(p[element].bf_trans_kd), &(q[element].bf_trans_kd), 1);

        __float_clone_array(&(p[element].bf_trans_Tf), &(q[element].bf_trans_Tf), 1);

        __float_clone_array(&(p[element].bf_rot_kp), &(q[element].bf_rot_kp), 1);

        __float_clone_array(&(p[element].bf_rot_ki), &(q[element].bf_rot_ki), 1);

        __float_clone_array(&(p[element].bf_rot_kd), &(q[element].bf_rot_kd), 1);

        __float_clone_array(&(p[element].bf_rot_Tf), &(q[element].bf_rot_Tf), 1);

    }
    return 0;
}

pid_values_t *pid_values_t_copy(const pid_values_t *p)
{
    pid_values_t *q = (pid_values_t*) malloc(sizeof(pid_values_t));
    __pid_values_t_clone_array(p, q, 1);
    return q;
}

void pid_values_t_destroy(pid_values_t *p)
{
    __pid_values_t_decode_array_cleanup(p, 1);
    free(p);
}

int pid_values_t_publish(lcm_t *lc, const char *channel, const pid_values_t *p)
{
      int max_data_size = pid_values_t_encoded_size (p);
      uint8_t *buf = (uint8_t*) malloc (max_data_size);
      if (!buf) return -1;
      int data_size = pid_values_t_encode (buf, 0, max_data_size, p);
      if (data_size < 0) {
          free (buf);
          return data_size;
      }
      int status = lcm_publish (lc, channel, buf, data_size);
      free (buf);
      return status;
}

struct _pid_values_t_subscription_t {
    pid_values_t_handler_t user_handler;
    void *userdata;
    lcm_subscription_t *lc_h;
};
static
void pid_values_t_handler_stub (const lcm_recv_buf_t *rbuf,
                            const char *channel, void *userdata)
{
    int status;
    pid_values_t p;
    memset(&p, 0, sizeof(pid_values_t));
    status = pid_values_t_decode (rbuf->data, 0, rbuf->data_size, &p);
    if (status < 0) {
        fprintf (stderr, "error %d decoding pid_values_t!!!\n", status);
        return;
    }

    pid_values_t_subscription_t *h = (pid_values_t_subscription_t*) userdata;
    h->user_handler (rbuf, channel, &p, h->userdata);

    pid_values_t_decode_cleanup (&p);
}

pid_values_t_subscription_t* pid_values_t_subscribe (lcm_t *lcm,
                    const char *channel,
                    pid_values_t_handler_t f, void *userdata)
{
    pid_values_t_subscription_t *n = (pid_values_t_subscription_t*)
                       malloc(sizeof(pid_values_t_subscription_t));
    n->user_handler = f;
    n->userdata = userdata;
    n->lc_h = lcm_subscribe (lcm, channel,
                                 pid_values_t_handler_stub, n);
    if (n->lc_h == NULL) {
        fprintf (stderr,"couldn't reg pid_values_t LCM handler!\n");
        free (n);
        return NULL;
    }
    return n;
}

int pid_values_t_subscription_set_queue_capacity (pid_values_t_subscription_t* subs,
                              int num_messages)
{
    return lcm_subscription_set_queue_capacity (subs->lc_h, num_messages);
}

int pid_values_t_unsubscribe(lcm_t *lcm, pid_values_t_subscription_t* hid)
{
    int status = lcm_unsubscribe (lcm, hid->lc_h);
    if (0 != status) {
        fprintf(stderr,
           "couldn't unsubscribe pid_values_t_handler %p!\n", hid);
        return -1;
    }
    free (hid);
    return 0;
}
