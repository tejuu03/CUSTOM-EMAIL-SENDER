from googleapiclient.discovery import build
import json

def fetch_google_sheet(spreadsheet_id, range_name):
    service = build('sheets', 'v4')
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    headers = result.get('values', [])[0]  # First row as headers
    data = result.get('values', [])[1:]  # Remaining rows as data
    return headers, data

