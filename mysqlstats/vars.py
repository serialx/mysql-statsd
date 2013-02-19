mysql_variables = {
'aborted_clients': ['gauge', 0],
'aborted_connects': ['gauge', 0],
'binlog_cache_disk_use': ['gauge', 0],
'binlog_cache_use': ['gauge', 0],
'binlog_stmt_cache_disk_use': ['gauge', 0],
'binlog_stmt_cache_use': ['gauge', 0],
'bytes_received': ['gauge', 0],
'bytes_sent': ['gauge', 0],
'com_admin_commands': ['gauge', 0],
'com_assign_to_keycache': ['gauge', 0],
'com_alter_db': ['gauge', 0],
'com_alter_db_upgrade': ['gauge', 0],
'com_alter_event': ['gauge', 0],
'com_alter_function': ['gauge', 0],
'com_alter_procedure': ['gauge', 0],
'com_alter_server': ['gauge', 0],
'com_alter_table': ['gauge', 0],
'com_alter_tablespace': ['gauge', 0],
'com_analyze': ['gauge', 0],
'com_begin': ['gauge', 0],
'com_binlog': ['gauge', 0],
'com_call_procedure': ['gauge', 0],
'com_change_db': ['gauge', 0],
'com_change_master': ['gauge', 0],
'com_check': ['gauge', 0],
'com_checksum': ['gauge', 0],
'com_commit': ['gauge', 0],
'com_create_db': ['gauge', 0],
'com_create_event': ['gauge', 0],
'com_create_function': ['gauge', 0],
'com_create_index': ['gauge', 0],
'com_create_procedure': ['gauge', 0],
'com_create_server': ['gauge', 0],
'com_create_table': ['gauge', 0],
'com_create_trigger': ['gauge', 0],
'com_create_udf': ['gauge', 0],
'com_create_user': ['gauge', 0],
'com_create_view': ['gauge', 0],
'com_dealloc_sql': ['gauge', 0],
'com_delete': ['gauge', 0],
'com_delete_multi': ['gauge', 0],
'com_do': ['gauge', 0],
'com_drop_db': ['gauge', 0],
'com_drop_event': ['gauge', 0],
'com_drop_function': ['gauge', 0],
'com_drop_index': ['gauge', 0],
'com_drop_procedure': ['gauge', 0],
'com_drop_server': ['gauge', 0],
'com_drop_table': ['gauge', 0],
'com_drop_trigger': ['gauge', 0],
'com_drop_user': ['gauge', 0],
'com_drop_view': ['gauge', 0],
'com_empty_query': ['gauge', 0],
'com_execute_sql': ['gauge', 0],
'com_flush': ['gauge', 0],
'com_grant': ['gauge', 0],
'com_ha_close': ['gauge', 0],
'com_ha_open': ['gauge', 0],
'com_ha_read': ['gauge', 0],
'com_help': ['gauge', 0],
'com_insert': ['gauge', 0],
'com_insert_select': ['gauge', 0],
'com_install_plugin': ['gauge', 0],
'com_kill': ['gauge', 0],
'com_load': ['gauge', 0],
'com_lock_tables': ['gauge', 0],
'com_optimize': ['gauge', 0],
'com_preload_keys': ['gauge', 0],
'com_prepare_sql': ['gauge', 0],
'com_purge': ['gauge', 0],
'com_purge_before_date': ['gauge', 0],
'com_release_savepoint': ['gauge', 0],
'com_rename_table': ['gauge', 0],
'com_rename_user': ['gauge', 0],
'com_repair': ['gauge', 0],
'com_replace': ['gauge', 0],
'com_replace_select': ['gauge', 0],
'com_reset': ['gauge', 0],
'com_resignal': ['gauge', 0],
'com_revoke': ['gauge', 0],
'com_revoke_all': ['gauge', 0],
'com_rollback': ['gauge', 0],
'com_rollback_to_savepoint': ['gauge', 0],
'com_savepoint': ['gauge', 0],
'com_select': ['gauge', 0],
'com_set_option': ['gauge', 0],
'com_signal': ['gauge', 0],
'com_show_authors': ['gauge', 0],
'com_show_binlog_events': ['gauge', 0],
'com_show_binlogs': ['gauge', 0],
'com_show_charsets': ['gauge', 0],
'com_show_client_statistics': ['gauge', 0],
'com_show_collations': ['gauge', 0],
'com_show_contributors': ['gauge', 0],
'com_show_create_db': ['gauge', 0],
'com_show_create_event': ['gauge', 0],
'com_show_create_func': ['gauge', 0],
'com_show_create_proc': ['gauge', 0],
'com_show_create_table': ['gauge', 0],
'com_show_create_trigger': ['gauge', 0],
'com_show_databases': ['gauge', 0],
'com_show_engine_logs': ['gauge', 0],
'com_show_engine_mutex': ['gauge', 0],
'com_show_engine_status': ['gauge', 0],
'com_show_events': ['gauge', 0],
'com_show_errors': ['gauge', 0],
'com_show_fields': ['gauge', 0],
'com_show_function_status': ['gauge', 0],
'com_show_grants': ['gauge', 0],
'com_show_index_statistics': ['gauge', 0],
'com_show_keys': ['gauge', 0],
'com_show_master_status': ['gauge', 0],
'com_show_open_tables': ['gauge', 0],
'com_show_plugins': ['gauge', 0],
'com_show_privileges': ['gauge', 0],
'com_show_procedure_status': ['gauge', 0],
'com_show_processlist': ['gauge', 0],
'com_show_profile': ['gauge', 0],
'com_show_profiles': ['gauge', 0],
'com_show_relaylog_events': ['gauge', 0],
'com_show_slave_hosts': ['gauge', 0],
'com_show_slave_status': ['gauge', 0],
'com_show_slave_status_nolock': ['gauge', 0],
'com_show_status': ['gauge', 0],
'com_show_storage_engines': ['gauge', 0],
'com_show_table_statistics': ['gauge', 0],
'com_show_table_status': ['gauge', 0],
'com_show_tables': ['gauge', 0],
'com_show_temporary_tables': ['gauge', 0],
'com_show_thread_statistics': ['gauge', 0],
'com_show_triggers': ['gauge', 0],
'com_show_user_statistics': ['gauge', 0],
'com_show_variables': ['gauge', 0],
'com_show_warnings': ['gauge', 0],
'com_slave_start': ['gauge', 0],
'com_slave_stop': ['gauge', 0],
'com_stmt_close': ['gauge', 0],
'com_stmt_execute': ['gauge', 0],
'com_stmt_fetch': ['gauge', 0],
'com_stmt_prepare': ['gauge', 0],
'com_stmt_reprepare': ['gauge', 0],
'com_stmt_reset': ['gauge', 0],
'com_stmt_send_long_data': ['gauge', 0],
'com_truncate': ['gauge', 0],
'com_uninstall_plugin': ['gauge', 0],
'com_unlock_tables': ['gauge', 0],
'com_update': ['gauge', 0],
'com_update_multi': ['gauge', 0],
'com_xa_commit': ['gauge', 0],
'com_xa_end': ['gauge', 0],
'com_xa_prepare': ['gauge', 0],
'com_xa_recover': ['gauge', 0],
'com_xa_rollback': ['gauge', 0],
'com_xa_start': ['gauge', 0],
'connections': ['gauge', 0],
'created_tmp_disk_tables': ['gauge', 0],
'created_tmp_files': ['gauge', 0],
'created_tmp_tables': ['gauge', 0],
'delayed_errors': ['gauge', 0],
'delayed_insert_threads': ['gauge', 0],
'delayed_writes': ['gauge', 0],
'flush_commands': ['gauge', 0],
'handler_commit': ['gauge', 0],
'handler_delete': ['gauge', 0],
'handler_discover': ['gauge', 0],
'handler_prepare': ['gauge', 0],
'handler_read_first': ['gauge', 0],
'handler_read_key': ['gauge', 0],
'handler_read_last': ['gauge', 0],
'handler_read_next': ['gauge', 0],
'handler_read_prev': ['gauge', 0],
'handler_read_rnd': ['gauge', 0],
'handler_read_rnd_next': ['gauge', 0],
'handler_rollback': ['gauge', 0],
'handler_savepoint': ['gauge', 0],
'handler_savepoint_rollback': ['gauge', 0],
'handler_update': ['gauge', 0],
'handler_write': ['gauge', 0],
'innodb_adaptive_hash_cells': ['gauge', 0],
'innodb_adaptive_hash_heap_buffers': ['gauge', 0],
'innodb_adaptive_hash_hash_searches': ['gauge', 0],
'innodb_adaptive_hash_non_hash_searches': ['gauge', 0],
'innodb_background_log_sync': ['gauge', 0],
'innodb_buffer_pool_pages_data': ['gauge', 0],
'innodb_buffer_pool_pages_dirty': ['gauge', 0],
'innodb_buffer_pool_pages_flushed': ['gauge', 0],
'innodb_buffer_pool_pages_lru_flushed': ['gauge', 0],
'innodb_buffer_pool_pages_free': ['gauge', 0],
'innodb_buffer_pool_pages_made_not_young': ['gauge', 0],
'innodb_buffer_pool_pages_made_young': ['gauge', 0],
'innodb_buffer_pool_pages_misc': ['gauge', 0],
'innodb_buffer_pool_pages_old': ['gauge', 0],
'innodb_buffer_pool_pages_total': ['gauge', 0],
'innodb_buffer_pool_read_ahead_rnd': ['gauge', 0],
'innodb_buffer_pool_read_ahead': ['gauge', 0],
'innodb_buffer_pool_read_ahead_evicted': ['gauge', 0],
'innodb_buffer_pool_read_requests': ['gauge', 0],
'innodb_buffer_pool_reads': ['gauge', 0],
'innodb_buffer_pool_wait_free': ['gauge', 0],
'innodb_buffer_pool_write_requests': ['gauge', 0],
'innodb_checkpoint_age': ['gauge', 0],
'innodb_checkpoint_max_age': ['gauge', 0],
'innodb_checkpoint_target_age': ['gauge', 0],
'innodb_data_fsyncs': ['gauge', 0],
'innodb_data_pending_fsyncs': ['gauge', 0],
'innodb_data_pending_reads': ['gauge', 0],
'innodb_data_pending_writes': ['gauge', 0],
'innodb_data_read': ['gauge', 0],
'innodb_data_reads': ['gauge', 0],
'innodb_data_writes': ['gauge', 0],
'innodb_data_written': ['gauge', 0],
'innodb_dblwr_pages_written': ['gauge', 0],
'innodb_dblwr_writes': ['gauge', 0],
'innodb_deadlocks': ['gauge', 0],
'innodb_dict_tables': ['gauge', 0],
'innodb_history_list_length': ['gauge', 0],
'innodb_ibuf_discarded_delete_marks': ['gauge', 0],
'innodb_ibuf_discarded_deletes': ['gauge', 0],
'innodb_ibuf_discarded_inserts': ['gauge', 0],
'innodb_ibuf_free_list': ['gauge', 0],
'innodb_ibuf_merged_delete_marks': ['gauge', 0],
'innodb_ibuf_merged_deletes': ['gauge', 0],
'innodb_ibuf_merged_inserts': ['gauge', 0],
'innodb_ibuf_merges': ['gauge', 0],
'innodb_ibuf_segment_size': ['gauge', 0],
'innodb_ibuf_size': ['gauge', 0],
'innodb_log_waits': ['gauge', 0],
'innodb_log_write_requests': ['gauge', 0],
'innodb_log_writes': ['gauge', 0],
'innodb_lsn_current': ['gauge', 0],
'innodb_lsn_flushed': ['gauge', 0],
'innodb_lsn_last_checkpoint': ['gauge', 0],
'innodb_master_thread_1_second_loops': ['gauge', 0],
'innodb_master_thread_10_second_loops': ['gauge', 0],
'innodb_master_thread_background_loops': ['gauge', 0],
'innodb_master_thread_main_flush_loops': ['gauge', 0],
'innodb_master_thread_sleeps': ['gauge', 0],
'innodb_max_trx_id': ['gauge', 0],
'innodb_mem_adaptive_hash': ['gauge', 0],
'innodb_mem_dictionary': ['gauge', 0],
'innodb_mem_total': ['gauge', 0],
'innodb_mutex_os_waits': ['gauge', 0],
'innodb_mutex_spin_rounds': ['gauge', 0],
'innodb_mutex_spin_waits': ['gauge', 0],
'innodb_oldest_view_low_limit_trx_id': ['gauge', 0],
'innodb_os_log_fsyncs': ['gauge', 0],
'innodb_os_log_pending_fsyncs': ['gauge', 0],
'innodb_os_log_pending_writes': ['gauge', 0],
'innodb_os_log_written': ['gauge', 0],
'innodb_page_size': ['gauge', 0],
'innodb_pages_created': ['gauge', 0],
'innodb_pages_read': ['gauge', 0],
'innodb_pages_written': ['gauge', 0],
'innodb_purge_trx_id': ['gauge', 0],
'innodb_purge_undo_no': ['gauge', 0],
'innodb_row_lock_current_waits': ['gauge', 0],
'innodb_current_row_locks': ['gauge', 0],
'innodb_row_lock_time': ['gauge', 0],
'innodb_row_lock_time_avg': ['gauge', 0],
'innodb_row_lock_time_max': ['gauge', 0],
'innodb_row_lock_waits': ['gauge', 0],
'innodb_rows_deleted': ['gauge', 0],
'innodb_rows_inserted': ['gauge', 0],
'innodb_rows_read': ['gauge', 0],
'innodb_rows_updated': ['gauge', 0],
'innodb_s_lock_os_waits': ['gauge', 0],
'innodb_s_lock_spin_rounds': ['gauge', 0],
'innodb_s_lock_spin_waits': ['gauge', 0],
'innodb_truncated_status_writes': ['gauge', 0],
'innodb_x_lock_os_waits': ['gauge', 0],
'innodb_x_lock_spin_rounds': ['gauge', 0],
'innodb_x_lock_spin_waits': ['gauge', 0],
'key_blocks_not_flushed': ['gauge', 0],
'key_blocks_unused': ['gauge', 0],
'key_blocks_used': ['gauge', 0],
'key_read_requests': ['gauge', 0],
'key_reads': ['gauge', 0],
'key_write_requests': ['gauge', 0],
'key_writes': ['gauge', 0],
'last_query_cost': ['gauge', 0],
'max_used_connections': ['gauge', 0],
'not_flushed_delayed_rows': ['gauge', 0],
'open_files': ['gauge', 0],
'open_streams': ['gauge', 0],
'open_table_definitions': ['gauge', 0],
'open_tables': ['gauge', 0],
'opened_files': ['gauge', 0],
'opened_table_definitions': ['gauge', 0],
'opened_tables': ['gauge', 0],
'performance_schema_cond_classes_lost': ['gauge', 0],
'performance_schema_cond_instances_lost': ['gauge', 0],
'performance_schema_file_classes_lost': ['gauge', 0],
'performance_schema_file_handles_lost': ['gauge', 0],
'performance_schema_file_instances_lost': ['gauge', 0],
'performance_schema_locker_lost': ['gauge', 0],
'performance_schema_mutex_classes_lost': ['gauge', 0],
'performance_schema_mutex_instances_lost': ['gauge', 0],
'performance_schema_rwlock_classes_lost': ['gauge', 0],
'performance_schema_rwlock_instances_lost': ['gauge', 0],
'performance_schema_table_handles_lost': ['gauge', 0],
'performance_schema_table_instances_lost': ['gauge', 0],
'performance_schema_thread_classes_lost': ['gauge', 0],
'performance_schema_thread_instances_lost': ['gauge', 0],
'prepared_stmt_count': ['gauge', 0],
'qcache_free_blocks': ['gauge', 0],
'qcache_free_memory': ['gauge', 0],
'qcache_hits': ['gauge', 0],
'qcache_inserts': ['gauge', 0],
'qcache_lowmem_prunes': ['gauge', 0],
'qcache_not_cached': ['gauge', 0],
'qcache_queries_in_cache': ['gauge', 0],
'qcache_total_blocks': ['gauge', 0],
'queries': ['gauge', 0],
'questions': ['gauge', 0],
'select_full_join': ['gauge', 0],
'select_full_range_join': ['gauge', 0],
'select_range': ['gauge', 0],
'select_range_check': ['gauge', 0],
'select_scan': ['gauge', 0],
'slave_heartbeat_period': ['gauge', 0],
'slave_open_temp_tables': ['gauge', 0],
'slave_received_heartbeats': ['gauge', 0],
'slave_retried_transactions': ['gauge', 0],
'slow_launch_threads': ['gauge', 0],
'slow_queries': ['gauge', 0],
'sort_merge_passes': ['gauge', 0],
'sort_range': ['gauge', 0],
'sort_rows': ['gauge', 0],
'sort_scan': ['gauge', 0],
'table_locks_immediate': ['gauge', 0],
'table_locks_waited': ['gauge', 0],
'tc_log_max_pages_used': ['gauge', 0],
'tc_log_page_size': ['gauge', 0],
'tc_log_page_waits': ['gauge', 0],
'threads_cached': ['gauge', 0],
'threads_connected': ['gauge', 0],
'threads_created': ['gauge', 0],
'threads_running': ['gauge', 0],
'uptime': ['gauge', 0],
'uptime_since_flush_status': ['gauge', 0],
'binlog_commits': ['gauge', 0],
'binlog_group_commits': ['gauge', 0],
'wsrep_cluster_size': ['gauge', 0],
'mutex_spin_waits': ['gauge', 0],
'mutex_spin_rounds': ['gauge', 0],
'mutex_spin_oswaits': ['gauge', 0],
'rw_shared_spin_waits': ['gauge', 0],
'rw_shared_os_waits': ['gauge', 0],
'rw_excl_spin_waits': ['gauge', 0],
'rw_excl_os_waits': ['gauge', 0],
'rw_shared_spin_waits': ['gauge', 0],
'rw_shared_os_waits': ['gauge', 0],
'rw_excl_spin_waits': ['gauge', 0],
'rw_excl_os_waits': ['gauge', 0],
'innodb_transactions': ['gauge', 0],
'unpurged_transactions': ['gauge', 0],
'history_list_length': ['gauge', 0],
'read_views': ['gauge', 0],
'current_transactions': ['gauge', 0],
'active_transactions': ['gauge', 0],
'innodb_lock_wait_secs': ['gauge', 0],
'slave_running': ['gauge', 0],
'slave_io_running': ['gauge', 0],
'slave_sql_running': ['gauge', 0],
'seconds_behind_master': ['gauge', 0],
'relay_log_space': ['gauge', 0],
'innodb_tables_in_use': ['gauge', 0],
'innodb_locked_tables': ['gauge', 0],
'innodb_lock_structs': ['gauge', 0],
'locked_transactions': ['gauge', 0],
'file_reads': ['gauge', 0],
'file_writes': ['gauge', 0],
'file_fsyncs': ['gauge', 0],
'pending_normal_aio_reads': ['gauge', 0],
'pending_normal_aio_writes': ['gauge', 0],
'pending_ibuf_aio_reads': ['gauge', 0],
'pending_aio_log_ios': ['gauge', 0],
'pending_aio_sync_ios': ['gauge', 0],
'pending_log_flushes': ['gauge', 0],
'pending_buf_pool_flushes': ['gauge', 0],
'ibuf_used_cells': ['gauge', 0],
'ibuf_free_cells': ['gauge', 0],
'ibuf_cell_count': ['gauge', 0],
'ibuf_merges': ['gauge', 0],
'hash_index_cells_total': ['gauge', 0],
'log_writes': ['gauge', 0],
'hash_index_cells_used': ['gauge', 0],
'log_writes': ['gauge', 0],
'pending_log_writes': ['gauge', 0],
'pending_chkp_writes': ['gauge', 0],
'last_checkpoint': ['gauge', 0],
'total_mem_alloc': ['gauge', 0],
'additional_pool_alloc': ['gauge', 0],
'adaptive_hash_memory': ['gauge', 0],
'page_hash_memory': ['gauge', 0],
'dictionary_cache_memory': ['gauge', 0],
'file_system_memory': ['gauge', 0],
'lock_system_memory': ['gauge', 0],
'recovery_system_memory': ['gauge', 0],
'thread_hash_memory': ['gauge', 0],
'innodb_io_pattern_memory': ['gauge', 0],
'pool_size': ['gauge', 0],
'free_pages': ['gauge', 0],
'database_pages': ['gauge', 0],
'modified_pages': ['gauge', 0],
'pages_read': ['gauge', 0],
'pages_created': ['gauge', 0],
'pages_written': ['gauge', 0],
'rows_inserted': ['gauge', 0],
'rows_updated': ['gauge', 0],
'rows_deleted': ['gauge', 0],
'rows_read': ['gauge', 0],
'queries_inside': ['gauge', 0],
'queries_queued': ['gauge', 0],
'unflushed_log': ['gauge', 0],
'uncheckpointed_bytes': ['gauge', 0],
'log_bytes_flushed': ['gauge', 0],
'log_bytes_written': ['gauge', 0],
'unflushed_log': ['gauge', 0],
'uncheckpointed_bytes': ['gauge', 0],
'sleeping_queries': ['gauge', 0],
'long_queries': ['gauge', 0],
'processlist': ['gauge', 0],
'sending_queries': ['gauge', 0],
}
