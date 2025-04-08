from mcp.server.fastmcp import FastMCP
import datetime
from chinese_calendar import is_holiday, is_workday, get_holiday_detail, get_holidays, get_workdays

# Initialize FastMCP server
mcp = FastMCP("中国节假日日历")


@mcp.tool()
async def check_is_holiday(date: str):
    """判断一个日期是否是节假日
    
    Args:
        date (str): 日期字符串，格式为 YYYY-MM-DD
    """
    try:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if is_holiday(date_obj):
            return '%s 是节假日' % date
        else:
            return '%s 不是节假日' % date
    except ValueError:
        return '错误：请输入正确的日期格式 (YYYY-MM-DD)'


@mcp.tool()
async def check_is_workday(date: str):
    """判断一个日期是否是工作日
    Args:
        date (str): 日期字符串，格式为 YYYY-MM-DD
    """
    try:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if is_workday(date_obj):
            return '%s 是工作日' % date
        else:
            return '%s 不是工作日' % date
    except ValueError:
        return '错误：请输入正确的日期格式 (YYYY-MM-DD)'


@mcp.tool()
async def got_holiday_deatil(date: str):
    """获取指定日期的节假日详细信息
    
    Args:
        date (str): 日期字符串，格式为 YYYY-MM-DD
        
    Returns:
        tuple or None: 如果是节假日，返回一个元组 (节日名, 是否为假期)；如果不是节假日，返回 None
    """
    try:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        holiday_detail = get_holiday_detail(date_obj)
        return holiday_detail
    except ValueError:
        return '错误：请输入正确的日期格式 (YYYY-MM-DD)'

@mcp.tool()
async def got_holidays(start: str, end: str, include_weekend=True):
    """获取指定日期范围内的所有节假日，包括法定节假日和周末（如果include_weekend为True）
    Args:
        start (str): 开始日期，格式为 YYYY-MM-DD
        end (str): 结束日期，格式为 YYYY-MM-DD
        include_weekend (bool, optional): 是否包含周末. 默认为 True
        
    Returns:
        str: 返回所有节假日的日期字符串，多个日期之间以逗号和空格分隔
             例如: "2024-01-01, 2024-01-02, 2024-01-06, 2024-01-07"
             如果日期格式错误则返回错误提示
    """
    try:
        start_obj = datetime.datetime.strptime(start,"%Y-%m-%d").date()
        end_obj = datetime.datetime.strptime(end,"%Y-%m-%d").date()
        holidays = get_holidays(start_obj, end_obj, include_weekend)
        return ', '.join([date.strftime('%Y-%m-%d') for date in holidays])
    except ValueError:
        return '错误：请输入正确的日期格式 (YYYY-MM-DD)'

@mcp.tool()
async def got_workdays(start: str, end: str, include_weekend=True):
    """获取指定日期范围内的所有工作日
    
    Args:
        start (str): 开始日期，格式为 YYYY-MM-DD
        end (str): 结束日期，格式为 YYYY-MM-DD
        include_weekend (bool, optional): 是否包含周末. 默认为 True
        
    Returns:
        str: 返回所有工作日的日期字符串，多个日期之间以逗号和空格分隔
             例如: "2024-01-01, 2024-01-02, 2024-01-06, 2024-01-07"
             如果日期格式错误则返回错误提示
    """
    try:
        start_obj = datetime.datetime.strptime(start,"%Y-%m-%d").date()
        end_obj = datetime.datetime.strptime(end,"%Y-%m-%d").date()
        workdays = get_workdays(start_obj, end_obj, include_weekend)
        return ', '.join([date.strftime('%Y-%m-%d') for date in workdays])
    except ValueError:
        return '错误：请输入正确的日期格式 (YYYY-MM-DD)'



if __name__ == "__main__":
    mcp.run(transport='stdio')
