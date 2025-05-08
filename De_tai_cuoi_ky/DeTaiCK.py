import time, random, tkinter as tk
from collections import deque
from dataclasses import dataclass
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
#try:
from memory_profiler import memory_usage          # tuỳ chọn
#except ImportError:
#    memory_usage = lambda *_, **__: [0]               # fallback
from graphviz import Digraph

# ================================================================
# 1. AVL TREE IMPLEMENTATION
# ================================================================
#@dataclass(slots=True)
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.freq = 1
        self.left = None
        self.right = None
        self.h = 1

    def bump(self):              # Tăng tần suất
        self.freq += 1


class AVLTree:
    """AVL-balanced BST, hỗ trợ tần suất"""
    def __init__(self): self.root = None

    # ---------- internal helpers ----------
    def _h(self, n): return n.h if n else 0
    def _bal(self, n): return self._h(n.left) - self._h(n.right) if n else 0
    def _upd_h(self, n): n.h = max(self._h(n.left), self._h(n.right)) + 1

    def _rot_r(self, y):
        x, y.left = y.left, y.left.right
        x.right = y
        self._upd_h(y); self._upd_h(x); return x

    def _rot_l(self, x):
        y, x.right = x.right, x.right.left
        y.left = x
        self._upd_h(x); self._upd_h(y); return y

    # ---------- public ops ----------
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, n, k):
        if not n: return Node(k)
        if k == n.key: n.bump(); return n
        if k < n.key:  n.left  = self._insert(n.left,  k)
        else:          n.right = self._insert(n.right, k)

        self._upd_h(n)
        bal = self._bal(n)

        # four AVL cases
        if bal > 1 and k < n.left.key:  return self._rot_r(n)
        if bal < -1 and k > n.right.key:return self._rot_l(n)
        if bal > 1:                     n.left = self._rot_l(n.left);  return self._rot_r(n)
        if bal < -1:                    n.right= self._rot_r(n.right); return self._rot_l(n)
        return n

    def search(self, k):
        n = self.root
        while n and n.key != k:
            n = n.left if k < n.key else n.right
        return n

    def delete(self, k):               # giảm tần suất trước khi xoá
        self.root = self._delete(self.root, k)

    def _delete(self, n, k):
        if not n: return None
        if k < n.key:  n.left  = self._delete(n.left, k)
        elif k > n.key:n.right = self._delete(n.right, k)
        else:
            if n.freq > 1: n.freq -= 1; return n
            if not n.left: return n.right
            if not n.right:return n.left
            succ = self._min(n.right)
            n.key, n.freq = succ.key, succ.freq
            succ.freq = 1
            n.right = self._delete(n.right, succ.key)

        self._upd_h(n)
        bal = self._bal(n)
        if bal > 1 and self._bal(n.left) >= 0:  return self._rot_r(n)
        if bal > 1:                            n.left = self._rot_l(n.left);  return self._rot_r(n)
        if bal < -1 and self._bal(n.right)<=0: return self._rot_l(n)
        if bal < -1:                           n.right= self._rot_r(n.right); return self._rot_l(n)
        return n

    def _min(self, n):
        while n.left: n = n.left
        return n

    # ---------- traversals / utils ----------
    def level_order(self):
        if not self.root: return []
        q, out = deque([self.root]), []
        while q:
            n = q.popleft()
            out.append((n.key, n.freq))
            if n.left:  q.append(n.left)
            if n.right: q.append(n.right)
        return out

    def inorder_keys(self):
        keys=[]
        def _io(n):
            if n: _io(n.left); keys.append(n.key); _io(n.right)
        _io(self.root); return keys

    def elems_freq(self):
        res=[]
        def _walk(n):
            if n: res.append((n.key,n.freq)); _walk(n.left); _walk(n.right)
        _walk(self.root); return res

    # ---------- plotting ----------
    def plot(self, view=False):
        if not self.root:
            messagebox.showinfo('Info','Tree is empty'); return
        dot = Digraph('AVL')
        def add(n):
            if not n: return
            dot.node(str(id(n)), f'{n.key} ({n.freq})')
            if n.left:
                dot.edge(str(id(n)), str(id(n.left)))
                add(n.left)
            if n.right:
                dot.edge(str(id(n)), str(id(n.right)))
                add(n.right)
        add(self.root)
        dot.render('avl_tree', format='png', view=view, cleanup=True)

# ================================================================
# 2. SIMPLE FREQUENCY‑BASED SUGGESTER
# ================================================================
class FreqRanker:
    def __init__(self): self.data=[]
    def update(self, elems):          # elems = [(key,freq),...]
        self.data = sorted(elems, key=lambda x:-x[1])
    def suggest(self, k=5): return self.data[:k]

# ================================================================
# 3. PERFORMANCE COMPARISON
# ================================================================
def build_avl(data):
    tree = AVLTree()
    for v in data: tree.insert(v)
    return tree

def build_list(data):
    lst = []
    for v in data: lst.append(v)
    sorted_list = sorted(lst)
    return sorted_list

def bench(sizes=(100, 1000, 10000, 100000)):
    out=[]
    for n in sizes:
        data=list(range(n)); random.shuffle(data)

        t0=time.perf_counter()
        avl=build_avl(data)
        t_build_avl=time.perf_counter()-t0

        mem_avl=max(memory_usage((build_avl,(data,)),interval=0.1))

        t0=time.perf_counter()
        lst=build_list(data)
        t_build_lst=time.perf_counter()-t0

        mem_lst=max(memory_usage((build_list,(data,)),interval=0.1))

        # search 100 phần tử bất kỳ
        samples=random.sample(data, min(100,n))
        t_avl=t_lst=0
        for v in samples:
            t1=time.perf_counter(); avl.search(v);     t_avl+=time.perf_counter()-t1
            t1=time.perf_counter(); v in lst;         t_lst+=time.perf_counter()-t1
        out.append(dict(size=n,
                        avl_build=t_build_avl,
                        avl_search=t_avl/len(samples),
                        avl_mem=mem_avl,
                        lst_build=t_build_lst,
                        lst_search=t_lst/len(samples),
                        lst_mem=mem_lst))
    return out

# ================================================================
# 4. TKINTER GUI
# ================================================================
class BSTApp:
    def __init__(self, master: tk.Tk):
        self.master=master; master.title('AVL Tree GUI')
        master.geometry("500x300")
        self.tree=AVLTree(); self.rank=FreqRanker()

        # ---------- widgets ----------
        self.entry=tk.Entry(master);     self.entry.pack(pady=5)
        self.sug  =tk.Label(master, text='Ranks: None', wraplength=1000)
        self.sug.pack(pady=2)

        for txt,cmd in (
            ('Insert',  self.insert),
            ('Delete',  self.delete),
            ('Search',  self.search),
            ('Show tree',self.show_tree),
            ('Load file',self.load_file),
            ('Run Performance',self.run_performance),
            ('Clear',   self.clear),
        ):
            tk.Button(master,text=txt,command=cmd).pack(fill='x',padx=20,pady=2)

        self.entry.bind('<KeyRelease>', self._show_sug)

    # ---------- helpers ----------
    def _refresh_rank(self):
        self.rank.update(self.tree.elems_freq())
        self._show_sug()

    def _show_sug(self, *_):
        rec=self.rank.suggest()
        txt='Ranks: ' + ', '.join(f'{k} ({f}x)' for k,f in rec) if rec else 'Ranks: None'
        self.sug.config(text=txt)

    # ---------- callbacks ----------
    def insert(self):
        vals=self._parse_entry()
        for v in vals: self.tree.insert(v)
        self._refresh_rank()
        messagebox.showinfo('Success',f'Inserted {len(vals)} node')

    def delete(self):
        vals=self._parse_entry()
        for v in vals: self.tree.delete(v)
        self._refresh_rank()
        messagebox.showinfo('Success',f'Deleted {len(vals)} node')

    def search(self):
        vals=self._parse_entry()
        msg=''
        for v in vals:
            n=self.tree.search(v)
            msg+=f'{v}: {"Found" if n else "Not found"}\n'
        messagebox.showinfo('Result',msg.strip())

    def show_tree(self): self.tree.plot(view=True)

    def clear(self):
        self.tree=AVLTree(); self.rank.update([])
        self._show_sug(); messagebox.showinfo('Success','Tree is empty')

    def load_file(self):
        fp=filedialog.askopenfilename(filetypes=[('Text','*.txt *.csv')])
        if not fp: return
        cnt=0
        with open(fp,'r') as f:
            for line in f:
                for tok in line.replace(',',' ').split():
                    try: self.tree.insert(int(tok)); cnt+=1
                    except ValueError: pass
        self._refresh_rank()
        messagebox.showinfo('Success',f'Inserted {cnt} nodes from file')

    def run_performance(self):
        res=bench()
        self._show_result(res)

    # ---------- UI utils ----------
    def _parse_entry(self):
        txt=self.entry.get()
        self.entry.delete(0,'end')
        if not txt: raise ValueError('Please enter a valid')
        return [int(t) for t in txt.replace(',',' ').split()]

    def _show_result(self,res):
        w=tk.Toplevel(self.master); w.title('Performance Comparison Results')
        w.geometry("500x300")
        txt=''
        for r in res:
            txt+=(f"The number of elements: {r['size']}\n"
                  f"  AVL  Build:  {r['avl_build']:.6f}s;  Search: {r['avl_search']:.6f}s;  Mem: {r['avl_mem']:.1f} MiB\n"
                  f"  Sorted List Build:  {r['lst_build']:.6f}s;  Search: {r['lst_search']:.6f}s;  Mem: {r['lst_mem']:.1f} MiB\n\n")
        tk.Message(w,text=txt,width=550).pack(padx=10,pady=2)
        tk.Button(w,text='Charts', width=10, command=lambda:self._plot(res)).pack(pady=0)

    def _plot(self,res):
        sizes=[r['size'] for r in res]
        for metric,lab in (('build','Build Time (s)'),
                           ('search','Search Time (s)'),
                           ('mem','Memory (MiB)')):
            plt.figure(figsize=(8,5))
            plt.plot(sizes,[r[f'avl_{metric}'] for r in res],marker='o',label='AVL', color='blue')
            plt.plot(sizes,[r[f'lst_{metric}']  for r in res],marker='o',label='Sorted List', color='red')
            plt.xscale('log'); plt.xlabel('The number of elements', fontsize=12); plt.ylabel(lab, fontsize=12); plt.title(lab)
            plt.legend(); plt.grid(True); plt.tight_layout(); plt.savefig(f'perf_{metric}.png'); plt.close()
        messagebox.showinfo('Success','Saved file perf_*.png in current folder')

# ================================================================
# 5. MAIN
# ================================================================
if __name__ == '__main__':
    root=tk.Tk()
    BSTApp(root)
    root.mainloop()