# 将[lovable_dir_name]的文件夹中的核心文件 放入到next-fullstack-template中

# 1. 要求用户输入[lovable_dir_name]
# 2. 将./[lovable_dir_name]/public/*复制到./next-fullstack-template/public/
# 3. 将./[lovable_dir_name]/src/components/*移动到./next-fullstack-template/components/*
# 4. 将./[lovable_dir_name]/src/剩下的所有的东西复制到./next-fullstack-template/components/app中

# 分清楚移动和复制

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lovable项目文件迁移脚本
将lovable项目的核心文件整理到next-fullstack-template中
"""

import os
import shutil
import sys
from pathlib import Path


def ensure_dir_exists(dir_path):
    """确保目录存在，如果不存在则创建"""
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"✓ 确保目录存在: {dir_path}")


def copy_files(src_dir, dest_dir, operation="复制"):
    """复制文件和文件夹"""
    if not os.path.exists(src_dir):
        print(f"⚠️  源目录不存在: {src_dir}")
        return False
    
    ensure_dir_exists(dest_dir)
    
    # 复制目录下的所有内容
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_item):
            if os.path.exists(dest_item):
                shutil.rmtree(dest_item)
            shutil.copytree(src_item, dest_item)
            print(f"✓ {operation}目录: {src_item} -> {dest_item}")
        else:
            shutil.copy2(src_item, dest_item)
            print(f"✓ {operation}文件: {src_item} -> {dest_item}")
    
    return True


def move_files(src_dir, dest_dir):
    """移动文件和文件夹"""
    if not os.path.exists(src_dir):
        print(f"⚠️  源目录不存在: {src_dir}")
        return False
    
    ensure_dir_exists(dest_dir)
    
    # 移动目录下的所有内容
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.exists(dest_item):
            if os.path.isdir(dest_item):
                shutil.rmtree(dest_item)
            else:
                os.remove(dest_item)
        
        shutil.move(src_item, dest_item)
        print(f"✓ 移动: {src_item} -> {dest_item}")
    
    return True


def copy_remaining_src_files(src_dir, dest_dir, exclude_dirs=None):
    """复制src目录下除了指定目录外的所有内容"""
    if exclude_dirs is None:
        exclude_dirs = ['components']
    
    if not os.path.exists(src_dir):
        print(f"⚠️  源目录不存在: {src_dir}")
        return False
    
    ensure_dir_exists(dest_dir)
    
    for item in os.listdir(src_dir):
        if item in exclude_dirs:
            print(f"⏭️  跳过目录: {item}")
            continue
            
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_item):
            if os.path.exists(dest_item):
                shutil.rmtree(dest_item)
            shutil.copytree(src_item, dest_item)
            print(f"✓ 复制目录: {src_item} -> {dest_item}")
        else:
            shutil.copy2(src_item, dest_item)
            print(f"✓ 复制文件: {src_item} -> {dest_item}")
    
    return True


def main():
    print("🚀 Lovable项目文件迁移脚本")
    print("=" * 50)
    
    # 1. 获取用户输入的目录名
    lovable_dir_name = input("请输入lovable项目目录名 [lovable_dir_name]: ").strip()
    
    if not lovable_dir_name:
        print("❌ 错误: 请输入有效的目录名")
        sys.exit(1)
    
    # 检查源目录是否存在
    if not os.path.exists(lovable_dir_name):
        print(f"❌ 错误: 源目录 '{lovable_dir_name}' 不存在")
        sys.exit(1)
    
    # 检查目标模板目录是否存在
    template_dir = "next-fullstack-template"
    if not os.path.exists(template_dir):
        print(f"❌ 错误: 目标模板目录 '{template_dir}' 不存在")
        sys.exit(1)
    
    print(f"\n📁 源目录: {lovable_dir_name}")
    print(f"📁 目标目录: {template_dir}")
    
    # 确认操作
    confirm = input("\n是否继续执行迁移操作? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes', '是']:
        print("❌ 操作已取消")
        sys.exit(0)
    
    print("\n🔄 开始执行迁移操作...")
    print("-" * 50)
    
    try:
        # 2. 复制 public 目录
        print("\n📂 步骤1: 复制public目录")
        src_public = os.path.join(lovable_dir_name, "public")
        dest_public = os.path.join(template_dir, "public")
        copy_files(src_public, dest_public, "复制")
        
        # 3. 移动 components 目录
        print("\n📂 步骤2: 移动components目录")
        src_components = os.path.join(lovable_dir_name, "src", "components")
        dest_components = os.path.join(template_dir, "components")
        move_files(src_components, dest_components)
        
        # 4. 复制src目录下的其余内容到components/app
        print("\n📂 步骤3: 复制src剩余内容到components/app")
        src_remaining = os.path.join(lovable_dir_name, "src")
        dest_app = os.path.join(template_dir, "components", "app")
        copy_remaining_src_files(src_remaining, dest_app, exclude_dirs=['components'])
        
        print("\n" + "=" * 50)
        print("✅ 迁移操作完成!")
        print(f"📁 所有文件已成功迁移到 {template_dir}")
        
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
