#ifndef MAHO_BASE_PNT2_H
#define MAHO_BASE_PNT2_H

#include <iostream>
#include <maho/base/vec2.h>

namespace maho
{
    template <typename T> class pnt2 : public vec2<T>
    {
    public:
        constexpr pnt2() : vec3<T>() {}
        constexpr pnt2(T x, T y) : vec3<T>(x, y) {}
        constexpr pnt2(const pnt2 &p) : vec3<T>(p) {}
        constexpr pnt2(const vec2<T> &v) : vec3<T>(v) {}
        constexpr pnt2 &operator=(const pnt2 &p)
        {
            vec2<T>::operator=(p);
            return *this;
        }
        constexpr pnt3 &operator=(const vec2<T> &v)
        {
            vec2<T>::operator=(v);
            return *this;
        }
    };
}

#endif // MAHO_BASE_PNT2_H