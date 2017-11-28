#����ƪ

NumPy����Ҫ������ͬ��Ԫ�صĶ�ά���顣����һ�����е�Ԫ�ض���һ�����͡�ͨ��һ��������Ԫ��������Ԫ�ر���(ͨ����Ԫ��������)����NumPy��ά��(dimensions)������(axes)����ĸ���������(rank)��

�����������Ϊ2(��������ά��).��һ��ά�ȳ���Ϊ2,�ڶ���ά�ȳ���Ϊ3.

[[ 1., 0., 0.],
 [ 0., 1., 2.]]
NumPy�������౻���� ndarray ������Ҫndarray���������У�

ndarray.ndim ������ĸ�������python�������У���ĸ�����������
ndarray.shape �����ά�ȡ�����һ��ָʾ������ÿ��ά���ϴ�С������Ԫ�顣����һ��n��m�еľ�������shape���Խ���(2,3),���Ԫ��ĳ�����Ȼ���ȣ���ά�Ȼ���ndim����
ndarray.size ����Ԫ�ص��ܸ���������shape������Ԫ��Ԫ�صĳ˻���
ndarray.dtype һ����������������Ԫ�����͵Ķ��󣬿���ͨ�������ָ��dtypeʹ�ñ�׼Python���͡�����NumPy�ṩ���Լ����������͡�
ndarray.itemsize ������ÿ��Ԫ�ص��ֽڴ�С�����磬һ��Ԫ������Ϊfloat64������itemsiz����ֵΪ8(=64/8),���磬һ��Ԫ������Ϊcomplex32������item����Ϊ4(=32/8).
ndarray.data ����ʵ������Ԫ�صĻ�������ͨ�����ǲ���Ҫʹ��������ԣ���Ϊ��������ͨ��������ʹ�������е�Ԫ�ء�
��������

np.array(list)����np.array(tuple)
zeros��ones�Լ�empty
arrange(start,end,step)
linspace(start,end,number)
rand	�Լ�randn
fromfunction
>>> np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])
��������

��������������ǰ�Ԫ�صġ��µ����鱻�������ұ������䡣 ��������������ԣ�NumPy�еĳ˷������ * ָʾ��Ԫ�ؼ��㣬����˷�����ʹ�� dot �����򴴽��������ʵ��(�μ��̳��еľ����½�) ��������ǲ�ͬ���͵�����ʱ���������͸��ձ�;�ȷ����֪(������Ϊ����upcast)��

��Щ����Ĭ��Ӧ�õ��������������һ��������ɵ��б����޹��������״��Ȼ����ָ�� axis ��������԰�����Ӧ�õ�����ָ��������(axis=0 �Ƕ�һ��Ԫ��������)

ͨ�ú���

NumPy�ṩ��������ѧ������ sin , cos �� exp ����NumPy�У���Щ������ͨ�ú�����(ufunc)����NumPy����Щ�������ð������Ԫ�����㣬����һ��������Ϊ�����

������Ƭ�͵���

һά����

���б��÷�һ�� ����a[2:5]����a[ : :-1]����a[:6:2] = -1000

��ά����

��ά �������ÿ������һ����������Щ������һ�����ŷָ��Ԫ������� �������������������ṩʱ��ȷʧ����������Ϊ��������Ƭ��

b[-1]                                  # the last row. Equivalent to b[-1,:]
array([40, 41, 42, 43])

b[i] �������еı���ʽ������ i ��һϵ�� : ��������ʣ�µ��ᡣNumPyҲ������ʹ�á��㡱�� b[i,...] ���� (��)�����������һ������������Ԫ���Ҫ�ķֺš�

���� ��ά�����Ǿ͵�һ������Ե�: Ȼ�������һ�������ÿ��������Ԫ�ؽ������㣬���ǿ���ʹ��flat���ԣ�������������Ԫ�ص�һ��������:

��״����

������״

ravel()��reshape�Լ�resize reshape �����ı������״������������ resize �����ı����������� ����ڸı���״������һ��ά�ȱ�����-1����ά�Ƚ��Զ�������
####�����(��ϲ�ͬ������)

vstack ��hstack
���� column_stack ���н�һά����ϳɶ�ά���飬����ͬ�� vstack ��һά���顣row_stack ��������һ���棬��һά����������ϳɶ�ά���顣
����Щά�ȱȶ�ά���ߵ����飬 hstack ���ŵڶ�������ϣ� vstack ���ŵ�һ�������, concatenate ������ѡ�����������ʱ���ŵ��ᡣ
�ڸ�������£� r_[] �� c_[] �Դ�������һ��������ϵ��������ã�����������Χ����(��:��):
>>> r_[1:4,0,4]
array([1, 2, 3, 0, 4])
��һ������ָ�(split)�ɼ���С����

hsplit(a,3) # Split a into 3
hsplit(a,(3,4)) # Split a after the third and the fourth column
vsplit �����������ָ array split ����ָ�����ĸ���ָ
���ƺ���ͼ

����ȫ����

�򵥵ĸ�ֵ�����������������ǵ����ݡ�

Python ���ݲ���������Ϊ�ο� �����Ժ������ò��������顣

>>> a = arange(12)
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True
>>> b.shape = 3,4    # changes the shape of a
>>> a.shape
(3, 4)
��ͼ(view)��ǳ����

��ͬ������������ͬһ�����ݡ���ͼ��������һ���µ��������ָ��ͬһ���ݡ�

>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c.shape = 2,6                      # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0,4] = 1234                      # a's data changes
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
��Ƭ���鷵������һ����ͼ��

���

������Ʒ�����ȫ����������������ݡ�

>>> d = a.copy()                          # a new array object with new data is created
>>> d is a
False
>>> d.base is a                           # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
��������

�����ͷ���(method)����

��������
arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r , zeros, zeros_like 
ת��
astype, atleast 1d, atleast 2d, atleast 3d, mat 
����
array split, column stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack 
ѯ��
all, any, nonzero, where 
����
argmax, argmin, argsort, max, min, ptp, searchsorted, sort 
����
choose, compress, cumprod, cumsum, inner, fill, imag, prod, put, putmask, real, sum 
����ͳ��
cov, mean, std, var 
�������Դ���
cross, dot, outer, svd, vdot
����

�㲥����

�㲥������ʹͨ�ú���������ش�����������ͬ��״�����롣

�㲥��һ�����ǣ�������е���������ά�Ȳ�����ͬ��һ����1�������ظ���������ά�Ƚ�С��������ֱ�����е�����ӵ��һ����ά�ȡ�

�㲥�ڶ�����ȷ������Ϊ1��������������ķ�����ֵغ������������Ǹ����������״�Ĵ�С����������˵�������Ǹ�ά�ȵ�����Ԫ�ص�ֵ��Ӧ��ͬ��

Ӧ�ù㲥����֮����������Ĵ�С����ƥ�䡣

���ڵ���������������

��������

һά��������

������������������ά����һ����

>>> a = arange(12)**2  
>>> j = array( [ [ 3, 4], [ 9, 7 ] ] )         # a bidimensional array of indices
>>> a[j]  # the same shape as j
array([[ 9, 16],
       [81, 49]])
��ά��������

������������a�Ƕ�ά��ʱ��ÿһ��Ψһ����������ָ��a�ĵ�һά ������ʾ��ͨ����ͼƬ��ǩ�õ�ɫ��ת����ɫ��ͼ��չʾ��������Ϊ�� a[j]

����Ҳ���Ը�������ֹһά��������ÿһά�����������������ͬ����״�� a[i,j] a[i,2] a[:,j] ע��һά����ĳ��ȱ��������Ҫ��Ƭ��ά�Ȼ���ĳ���һ�� ����д��l=[i,j];a[l]���ǲ���д��l=array([i,j]);a[l]

��Ҳ����ʹ������������ΪĿ������ֵ�� Ȼ������һ�������б������ظ�ʱ����ֵ�������ɣ���������ֵ

>>> a = arange(5)
>>> a[[0,0,2]]=[1,2,3]
>>> a
array([2, 1, 3, 3, 4])
ͨ��������������

ix_����

ix_ ��������Ϊ�˻�� ��Ԫ�� �Ľ����������ϲ�ͬ���������磬�������Ҫ����������a��b��cԪ����ɵ���Ԫ�������� a+b*c ��

>>> a = array([2,3,4,5])
>>> b = array([8,5,4])
>>> c = array([5,4,6,8,3])
>>> ax,bx,cx = ix_(a,b,c)
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
>>> result = ax+bx*cx
>>> result
array([[[42, 34, 50, 66, 26],
        [27, 22, 32, 42, 17],
        [22, 18, 26, 34, 14]],
       [[43, 35, 51, 67, 27],
        [28, 23, 33, 43, 18],
        [23, 19, 27, 35, 15]],
       [[44, 36, 52, 68, 28],
        [29, 24, 34, 44, 19],
        [24, 20, 28, 36, 16]],
       [[45, 37, 53, 69, 29],
        [30, 25, 35, 45, 20],
        [25, 21, 29, 37, 17]]])
>>> result[3,2,4]
17
>>> a[3]+b[2]*c[4]
17
���Դ���

������

�Զ�ά����ʹ��һ��ð�Ų���һ��һά���飬Ȼ�����������һ����ά���� ���磬һ�� M[2,:] ��Ƭ������һ����״Ϊ(1,4)�ľ������֮�£�һ���������Ƭ���ǲ���һ����Ϳ���ά�� 11 �����顣���磬���C��һ����ά���飬 C[...,1] ����һ����ά������� C[1,:,1] ����һ��һά���顣

���������ά�ȣ������ʡ��һ���ߴ磬�������Զ��Ƶ�������

�߼�

�Զ���ṹ����

ͨ�� NumPy Ҳ���Զ����� C ���������Ľṹ���͡��� NumPy �ж���ṹ�ķ������£�

����ṹ�������ƣ������ֶ����ƣ������ֶ��������͡�

student= dtype({'names':['name', 'age', 'weight'], 'formats':['S32', 'i','f']}, align = True)
���� student ���Զ���ṹ���͵����ƣ�ʹ�� dtype �����������ڵ�һ�������У� 'names' �� 'formats' ���ܸı䣬 names ���г����ǽṹ���ֶ����ƣ� formats ���г����Ƕ�Ӧ�ֶε��������͡� S32 ��ʾ 32 �ֽڳ��ȵ��ַ����� i ��ʾ 32 λ�������� f ��ʾ 32 λ���ȵĸ����������һ������Ϊ True ʱ����ʾҪ������ڴ���롣 �ڶ���ýṹ����֮�󣬾Ϳ��Զ����Ը�����ΪԪ�ص������� ��

a= array([(��Zhang��, 32, 75.5), (��Wang��, 24, 65.2)], dtype =student)